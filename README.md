Signa
=====

[![PyPi Version](https://img.shields.io/pypi/v/signa.svg)](https://pypi.python.org/pypi/signa)

Utility lib to create authorized requests for various services.

Supported services:

- AWS S3
- Digital Ocean Spaces
- Yandex Object storage
- Alibaba Cloud OSS

**Currently in alpha, use with caution!**

Install
-------

```bash
pip install signa
```

Usage example
-------------

```python
import os
import requests
import signa

AWS_S3_REGION = '...'
AWS_S3_BUCKET = '...'
AWS_S3_UPLOAD_ACCESS_KEY = '...'
AWS_S3_UPLOAD_SECRET_KEY = '...'

S3_SIGNA = signa.Factory(
    's3',
    region=AWS_S3_REGION,
    bucket=AWS_S3_BUCKET,
    payload='UNSIGNED-PAYLOAD',
    auth={
        'access_key': AWS_S3_UPLOAD_ACCESS_KEY,
        'secret_key': AWS_S3_UPLOAD_SECRET_KEY,
    })

CONTENT_TYPES = {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.mp4': 'video/mp4',
    '.json': 'application/json',
}


def put_file(*, key=None, path_or_data=None, make_public=True,
             s3_signa=S3_SIGNA):
    """Put file to S3 with signa example. Return uploaded URL.
    """
    ext = os.path.splitext(key)[1]
    headers = {
        'content-type': CONTENT_TYPES.get(ext, 'application/octet-stream')
    }
    if make_public:
        headers['x-amz-acl'] = 'public-read'

    signed = s3_signa.new(method='PUT', key=key, headers=headers)

    if isinstance(path_or_data, str):
        path = path_or_data
        with open(path, 'rb') as data_fp:
            response = requests.put(signed['url'],
                                    headers=signed['headers'],
                                    data=data_fp)
    else:
        data = path_or_data
        response = requests.put(signed['url'],
                                headers=signed['headers'],
                                data=data)

    if response.status_code == 200:
        print('put_file: OK')
        return signed['url']

    return None
```
