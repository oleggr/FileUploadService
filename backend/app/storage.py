import typing
import boto3
import config


class Storage:
    bucket_name = 'logfiles'

    def __init__(self):
        session = boto3.session.Session()
        self.s3 = session.client(
            service_name='s3',
            aws_access_key_id=config.access_key,
            aws_secret_access_key=config.secret_key,
            endpoint_url=config.endpoint,
        )

    def put(self, request_id: str, filename: str, data: typing.IO):
        self.s3.put_object(
            Bucket=self.bucket_name,
            Key=request_id + '/' + filename,
            Body=data
        )
