import datetime

import requests

from Globals import Globals
from authentication.token import Token


def get_in_today(token: Token):
    last_time: datetime.datetime = Globals.get_last_activity_date_notify()

    start_day: float
    if last_time is None:
        now_time = datetime.datetime.now()
        start_day = datetime.datetime(now_time.year, now_time.month, now_time.day, 1, 0, 0).timestamp()
    else:
        start_day = datetime.datetime(last_time.year, last_time.month, last_time.day, last_time.hour-3,
                                      last_time.minute, last_time.second+1).timestamp()

    url = "https://www.strava.com/api/v3/athlete/activities"
    params = {
        'after':  int(start_day),
        "access_token": token.token,
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
