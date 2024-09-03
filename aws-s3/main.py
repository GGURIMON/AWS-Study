import boto3
import boto3.session

# 변수 설정
REGION = 'ap-northeast-2'
MY_BUCKET_NAME = 'my-first-s3-bucket-gguri'
FILE_NAME = 'idol.jpg'
PATH = './'

session = boto3.session(profile_name= 'mfa')
s3_client = boto3.client('s3', region_name = REGION)

# 이미지 업로드
s3_client.upload_file(PATH + FILE_NAME, MY_BUCKET_NAME, 'idol.jpg')

# 객체 목록 확인
response = s3_client.list_objects_v2(Bucket = MY_BUCKET_NAME)

for obj in response.get('Contents', []):
    print(obj)

# 객체 다운로드
s3_client.download_file(MY_BUCKET_NAME, FILE_NAME, f'./downloaded{FILE_NAME}')

# 객체 삭제
s3_client.delete_object(Bucket = MY_BUCKET_NAME, Key = FILE_NAME)