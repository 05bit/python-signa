from typing import Any, Dict, Optional
from . import s3


def new(method: str, region: str = '', bucket: str = '',
    key: str = '', auth: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
    payload: Any = None,
) -> Dict[str, str]:
    return s3.new(
        method=method,
        region=region,
        bucket=bucket,
        key=key,
        auth=auth,
        headers=headers,
        payload=payload,
        endpoint='{region}.digitaloceanspaces.com'
    )
