from .aws import aws_headers

REGIONS = {
    'us-west-000', 'us-west-001', 'us-west-002',
    # TODO: add European region
}

def new(method=None, region=None, bucket=None, key=None,
        auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}

    assert region in REGIONS

    # headers['host'] = '%s.s3.%s.backblazeb2.com' % (bucket, region)

    # https://s3.<region>.backblazeb2.com/<bucket>
    headers['host'] = 's3.%s.backblazeb2.com' % region

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
