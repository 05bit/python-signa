from signa.providers import s3
from signa.providers import onesignal
from signa.providers import dospaces

PROVIDERS = {
    's3': s3.new,
    'onesignal': onesignal.new,
    'dospaces': dospaces.new,
}


def new(_provider, **kwargs):
    assert _provider in PROVIDERS, (
        "Unknown provider: '%s', available: %s" % (
            _provider, list(PROVIDERS.keys())
        )
    )
    return PROVIDERS[_provider](**kwargs)


class Factory:
    def __init__(self, _provider, **base_params):
        self._provider = _provider
        self.base_params = base_params

    def new(self, **kwargs):
        for k, v in self.base_params.items():
            kwargs.setdefault(k, v)
        return new(self._provider, **kwargs)


if __name__ == '__main__':
    import yaml
    import json
    import requests

    with open('config.yml', 'r') as f:
        config = yaml.load(f)

    access_key = config['s3']['access_key']
    secret_key = config['s3']['secret_key']
    signed = new(
        's3',
        method='PUT',
        region='eu-central-1',
        bucket='jokelikeme-fr',
        key='test.txt',
        payload='UNSIGNED-PAYLOAD',
        headers={
            'x-amz-acl': 'public-read',
        },
        auth={
            'access_key': access_key,
            'secret_key': secret_key,
        })

    print(json.dumps(signed, indent=2))
    print('\n')

    r = requests.put(signed['url'], headers=signed['headers'], data=b'xxxxxxxx')
    print(r.text)
    print('\n')

#     test_string = """
# AWS4-HMAC-SHA256
# 20150830T123600Z
# 20150830/us-east-1/service/aws4_request
# 816cd5b414d056048ba4f7c5386d6e0533120fb1fcfa93762cf0fc39e2cf19e0
# """.strip()
#     access_key = 'AKIDEXAMPLE'
#     secret_key = 'wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY'
#     date_only = '20150830'
#     date_key = _hmac(('AWS4' + secret_key).encode('utf-8'), date_only)
#     date_region_key = _hmac(date_key, 'us-east-1')
#     date_region_service_key = _hmac(date_region_key, 'service')
#     signing_key = _hmac(date_region_service_key, 'aws4_request')
#     print(test_string)
#     print("Calculated:\n%s" % _hmac(signing_key, test_string, hexdigest=True))
#     print("Must be:\nb97d918cfa904a5beff61c982a1b6f458b799221646efd99d3219ec94cdf2500")
