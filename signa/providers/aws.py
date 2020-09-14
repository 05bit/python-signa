import datetime
import hashlib
import hmac
import json
import urllib.parse
from signa.logger import get_logger

utcnow = datetime.datetime.utcnow

logger = get_logger(__name__)


def aws_headers(method=None, region=None, service=None, uri=None,
                auth=None, headers=None, payload=None):
    headers = headers.copy() if headers else {}

    access_key = auth['access_key']
    secret_key = auth['secret_key']
    timestamp = utcnow().strftime('%Y%m%dT%H%M%SZ')
    date_only = timestamp[:8]
    scope = '%s/%s/%s/aws4_request' % (date_only, region, service)

    if payload == 'UNSIGNED-PAYLOAD':
        payload_hash = 'UNSIGNED-PAYLOAD'
    elif payload:
        payload_hash = _sha256(payload)
    else:
        payload_hash = _sha256('')

    headers['x-amz-content-sha256'] = payload_hash
    headers['x-amz-date'] = timestamp

    if uri:
        uri_parts = urllib.parse.urlparse(uri)
        path = uri_parts.path
        query = uri_parts.query
    else:
        path = '/'
        query = ''

    headers_keys = sorted(list(headers.keys()))

    canonical_request = '\n'.join([
        method or 'GET',
        path,
        query,
        '\n'.join(['%s:%s' % (k.lower(), headers[k])
            for k in headers_keys]),
        '',
        ';'.join(headers_keys).lower(),
        payload_hash,
    ]).strip()

    logger.debug(canonical_request)

    str_to_sign = '\n'.join([
        'AWS4-HMAC-SHA256',
        timestamp,
        scope,
        _sha256(canonical_request),
    ])

    # logger.debug(str_to_sign)

    base_key = ('AWS4' + secret_key).encode('utf-8')
    date_key = _hmac(base_key, date_only)
    date_region_key = _hmac(date_key, region)
    date_region_service_key = _hmac(date_region_key, 's3')
    signing_key = _hmac(date_region_service_key, 'aws4_request')

    # logger.debug(signing_key)

    signature = _hmac(signing_key, str_to_sign, hexdigest=True)

    # logger.debug(signature)

    headers['Authorization'] = (
        'AWS4-HMAC-SHA256 '
        'Credential=%s/%s,'
        'SignedHeaders=%s,'
        'Signature=%s' % (
            access_key,
            scope,
            ';'.join(headers_keys),
            signature)
    )

    return headers


def _sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def _hmac(key, msg, hexdigest=False):
    h = hmac.new(key, msg=msg.encode('utf-8'),
                 digestmod=hashlib.sha256)
    if hexdigest:
        return h.hexdigest()
    else:
        return h.digest()
