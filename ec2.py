import boto3

# MFA 인즈을 받은 mfa 프로필로 세션 생성
session = boto3.Session(profile_name='mfa')

# 사용할 수 있는 서비스 확인
# print(session.get_available_services())

# AWS 서비스 중 ec2를 선택
ec2_client = session.client('ec2')

ec2_client.run_instances(
    ImageId = 'ami-008d41dbe16db6778',
    InstanceType = 't2.micro',
    KeyName = 'KeyPair-For-Demo-EC2',
    SecurityGroupIds = ['sg-07dd6e08a7164f47b'],
    SubnetId = 'subnet-032a9a8326a4ac382',
    MinCount = 1,
    MaxCount = 1
    )