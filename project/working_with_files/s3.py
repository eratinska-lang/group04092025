import boto3
from requests.packages import target

from working_with_files.working_with_binary_files import response

ACCESS_KEY = 'e13de50095d962888c357d437d0bc855'
SECRET_KEY = '92c703ef97a891d9dc79f3adb3ed484b18eacc6f9b3d5fb0c4bbe6f586d31c2e'

BUCKET_NAME = 'group04092025'
ENDPOINT = "https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com"
PUBLIC_URL = 'https://pub-f0b804e4a87c49ec9fa377abd59b7d70.r2.dev'
REGION_NAME = 'EEUR'

session = boto3.client(
    service_name='s3',
    region_name=REGION_NAME,
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

target_file_name = "images/RE/cute_dogs.jpeg"
session.upload_file("cute_dogs.jpeg", BUCKET_NAME, target_file_name)
print(f"{PUBLIC_URL}/{target_file_name}")

# response = session.list_objects_v2(Bucket=BUCKET_NAME)
# print(response)

#session.download_file(BUCKET_NAME, target_file_name, '5555.jpeg')