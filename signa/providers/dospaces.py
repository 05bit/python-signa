from .aws import sign_aws


def new(method=None, region=None, bucket=None, key=None,
        auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}

    headers['host'] = '%s.%s.digitaloceanspaces.com' % (bucket, region)

    if key:
        rel_url = '/%s' % key
    else:
        rel_url = '/'

    signature = sign_aws(
        method=method,
        region=region,
        service='s3',
        uri=rel_url,
        auth=auth,
        headers=headers,
        payload=payload
    )

    headers.update(signature)

    return {
        'url': 'https://%s%s' % (headers['host'], rel_url),
        'headers': headers,
    }
