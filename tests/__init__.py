import os
# import time
import unittest
from dotenv import load_dotenv, find_dotenv
import signa

load_dotenv(find_dotenv())

aws_region = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')
aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_s3_bucket = os.environ.get('AWS_S3_BUCKET')
onesignal_app_id = os.environ.get('ONESIGNAL_APP_ID')
onesignal_api_key = os.environ.get('ONESIGNAL_API_KEY')


class SignaTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_new_s3(self):
        key = 'test.txt'
        _ = signa.new(
            's3',
            method='PUT',
            region=aws_region,
            bucket=aws_s3_bucket,
            key=key,
            payload='UNSIGNED-PAYLOAD',
            headers={
                'x-amz-acl': 'public-read',
            },
            auth={
                'access_key': aws_access_key,
                'secret_key': aws_secret_key,
            })
        self.assertTrue(True)

    def test_new_onesignal(self):
        self.assertTrue(True)
