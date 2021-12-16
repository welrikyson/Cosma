import datetime

import requests

from authentication.token import Token


def get_token(code):
    url = "https://www.strava.com/api/v3/oauth/token"
    params = {
        'client_id': "75467",
        "client_secret": "e811ea22ccbf0ac2e39211de1f9e85b1e6960b24",
        "code": code,
        "grant_type": "authorization_code"
    }
    response = requests.post(url=url, params=params)
    response_json = response.json()
    print(response_json)
    token = Token()
    token.token = response_json["access_token"]
    token.refresh_token = response_json["refresh_token"]
    token.expires_at = datetime.datetime.fromtimestamp(response_json["expires_at"])
    token.expires_in = response_json["expires_in"]
    print(token.token)
    return token


def refresh_token(token : Token):
    url = "https://www.strava.com/api/v3/oauth/token"
    params = {
        'client_id': "75467",
        "client_secret": "e811ea22ccbf0ac2e39211de1f9e85b1e6960b24",
        "grant_type": "refresh_token",
        'refresh_token ': token.refresh_token
    }
    response = requests.post(url=url, params=params)
    response_json = response.json()
    print(response_json)
    token = Token()
    token.token = response_json["access_token"]
    token.refresh_token = response_json["refresh_token"]
    token.expires_at = datetime.datetime.fromtimestamp(response_json["expires_at"])
    token.expires_in = response_json["expires_in"]
    print(token.token)
    return token
