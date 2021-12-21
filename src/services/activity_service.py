from datetime import datetime, timedelta, date, time

import requests

from src.globals import Globals
from src.authentication.token import Token


def get_in_today(token: Token):
    last_time: datetime = Globals.get_last_activity_date_notify()

    start_day: float
    if last_time is None:
        start_day = datetime.combine(date.today(), time()) .timestamp()
    else:
        start_day = (last_time + timedelta(seconds=1)).timestamp()

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
