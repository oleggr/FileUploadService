import typing
import boto3

from app.logger import logger
from app.utils import ConfigLoader


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
        try:
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=request_id + '/' + filename,
                Body=data
            )
            logger.info(f'File "{filename}" for request "{request_id}" uploading finished.')
            return True
        except Exception as e:
            logger.alert(f'File "{filename}" for request "{request_id}" uploading failed with error "{e}".')
            return False

    # def check_object_exist(self, filename: str) -> bool:
    #     self.s3.head_object(filename)
    #     return True
