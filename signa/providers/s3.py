from .aws import sign_aws


def new(method=None, region=None, bucket=None, key=None,
        auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}
    # headers['host'] = '%s.s3.%s.amazonaws.com' % (bucket, region)
    headers['host'] = 's3-%s.amazonaws.com' % region
    if key:
        uri = '/%s/%s' % (bucket, key)
    else:
        uri = '/%s' % bucket
    headers.update(sign_aws(
        method=method,
        region=region,
        service='s3',
        uri=uri,
        auth=auth,
        headers=headers,
        payload=payload))
    return {
        'url': 'https://%s%s' % (headers['host'], uri),
        'headers': headers,
    }
