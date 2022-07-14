import time
import boto3
import typing

from app.logger import logger
from app.utils import ConfigLoader
from app.notifications import notificator

class Storage:
    bucket_name = 'logfiles'

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
            notificator.send_failed_email(request_id, e)
            return False

        if self.check_object_exist(filename=full_file_name):
            return True
        return False

    def check_object_exist(self, filename) -> bool:
        objs = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=filename)
        if 'Contents' not in objs:
            return False

        objs = objs['Contents']
        return len(objs) == 1 and objs[0]['Key'] == filename
