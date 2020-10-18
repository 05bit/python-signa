from .aws import aws_headers


def new(method=None, region=None, bucket=None, key=None,
        auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}

    assert (not region) or (region == 'ru-central1')

    headers['host'] = 'storage.yandexcloud.net'
    region = 'ru-central1'

    if key:
        rel_uri = '/%s/%s' % (bucket, key)
    else:
        rel_uri = '/%s' % bucket

    headers.update(aws_headers(
        method=method,
        region=region,
        service='s3',
        uri=rel_uri,
        auth=auth,
        headers=headers,
        payload=payload
    ))

    return {
        'url': 'https://%s%s' % (headers['host'], rel_uri),
        'headers': headers,
    }
