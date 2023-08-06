import os
import time
import boto3
import typing

from app.logger import logger
from app.utils import ConfigLoader
from app.notifications import notificator


class S3Storage:
    bucket_name = 'logfiles'
    buffer_folder = 'buffer'

    def __init__(self):
        session = boto3.session.Session()
        config = ConfigLoader.get_config()
        self.s3 = session.client(
            service_name='s3',
            aws_access_key_id=config.access_key,
            aws_secret_access_key=config.secret_key,
            endpoint_url=config.endpoint,
        )

    def put(self, request_id: str, filename: str, data: typing.IO) -> bool:
        full_file_name = request_id + '/' + filename
        file_exist = self.check_object_exist(filename=full_file_name)
        if file_exist:
            filename = f'{int(time.time())}_' + filename
            full_file_name = request_id + '/' + filename

        try:
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=full_file_name,
                Body=data
            )
            logger.info(f'File "{filename}" for request "{request_id}" uploading finished.')
        except Exception as e:
            logger.alert(f'File "{filename}" for request "{request_id}" uploading failed with error "{e}".')
            notificator.send_failed_email(request_id, str(e))
            return False

        if self.check_object_exist(filename=full_file_name):
            return True
        return False

    def get(self, request_id: str, filename: str):
        if not os.path.isdir(self.buffer_folder):
            os.mkdir(self.buffer_folder)

        local_filename = self.buffer_folder + '/' + filename
        s3_filename = request_id + '/' + filename
        try:
            self.s3.download_file(
                self.bucket_name,
                s3_filename,
                local_filename,
            )
        except Exception as e:
            logger.alert(f'File "{s3_filename}" for request downloading failed with error "{e}".')
            return False

        return local_filename

    def get_file_by_name(self, filename, ts: str = None):
        if not os.path.isdir(self.buffer_folder):
            os.mkdir(self.buffer_folder)

        local_filename = self.buffer_folder + '/' + filename.split('/')[1]
        try:
            self.s3.download_file(
                self.bucket_name,
                filename,
                local_filename,
            )
        except Exception as e:
            logger.alert(f'File "{filename}" for request downloading failed with error "{e}".')
            return False

        return local_filename

    def get_objects_in_subfolder(self, subfolder):
        files = []

        objs = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=subfolder)
        if 'Contents' not in objs:
            return False

        objs = objs['Contents']
        for obj in objs:
            files.append({
                'name': obj['Key'],
                'size': str(round(obj['Size'] / 1048583.20763, 2)) + ' MB',
                'created': obj['LastModified'].strftime('%H:%M:%S %d/%m/%Y'),
            })

        return files

    def check_object_exist(self, filename) -> bool:
        objs = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=filename)
        if 'Contents' not in objs:
            return False

        objs = objs['Contents']
        return len(objs) == 1 and objs[0]['Key'] == filename
