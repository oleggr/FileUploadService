import os
from minio import Minio

client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

if client.bucket_exists("test"):
    print("test exists")
else:
    print("test does not exist")

objects = client.list_objects('test', recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified)

# Put a file with default content-type, upon success prints the etag identifier computed by server.
try:
    with open('test.txt', 'rb') as file_data:
        file_stat = os.stat('test.txt')
        print(client.put_object('test', 'test.txt',
                               file_data))
except Exception as err:
    print(err)


objects = client.list_objects('test', recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified)
