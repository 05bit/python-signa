from typing import Any, Dict, Optional
from .aws import aws_headers


def new(method: str, region: str = '', bucket: str = '',
        key: str = '', auth: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        payload: Any = None,
        endpoint:str = 's3.{region}.amazonaws.com'
    ) -> Dict[str, str]:
    """
    Create new signature for S3 request.

    Returns
    -------
    Dictionary with `url` and `headers` keys.
    """
    headers = headers.copy() if headers else {}

    if endpoint and region:
        endpoint = endpoint.format(region=region)

    # Details on buckets URLs:
    # https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html
    # https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/
    headers['host'] = '{bucket}.{endpoint}'.format(
        bucket=bucket, endpoint=endpoint
    )

    rel_uri = '/{key}'.format(key=(key or '')).strip()

    headers.update(aws_headers(
        method=method,
        region=region,
        service='s3',
        uri=rel_uri,
        auth=auth,
        headers=headers,
        payload=payload
    ))

    url = 'https://{host}{rel_uri}'.format(
        host=headers['host'], rel_uri=rel_uri
    )

    return {'url': url, 'headers': headers}
