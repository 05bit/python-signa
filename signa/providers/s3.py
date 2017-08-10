from .aws import sign_aws


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
