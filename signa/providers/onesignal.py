import json


def new(app_id=None, api_key=None, api_method=None, **payload):
    if not all((app_id, api_key, api_method)):
        raise RuntimeError("Missing one or more of required arguments: "
                           "app_id, api_key, api_method")

    url = 'https://onesignal.com/api/v1/%s' % api_method
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Basic %s' % api_key
    }
    payload['app_id'] = app_id
    return {
        'url': url,
        'headers': headers,
        'data': json.dumps(payload)
    }
