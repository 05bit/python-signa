from .aws import aws_headers


def new(method=None, region=None, bucket=None, key=None,
        auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}

    headers['host'] = '%s.%s.digitaloceanspaces.com' % (bucket, region)

    rel_uri = ('/%s' % key) if key else '/'

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
