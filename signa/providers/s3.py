from .aws import aws_headers


def new(method=None, region=None, bucket=None, key=None,
        auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}

    # Details on buckets URLs:
    # http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html
    # if region and (region != 'us-east-1'):
    #     headers['host'] = 's3-%s.amazonaws.com' % region
    # else:
    #     headers['host'] = 's3.amazonaws.com'
    headers['host'] = 's3-%s.amazonaws.com' % region

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
