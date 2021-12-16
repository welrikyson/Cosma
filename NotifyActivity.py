import datetime

import requests


def notify_activity(activity):
    moving_time  = activity["moving_time"]
    seconds = moving_time % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    url = "https://docs.google.com/forms/d/e/1FAIpQLScAS9v785IGB71I7o6AlZgP34BgikUX2__UYCCwZqfRcV22Qw/formResponse"
    params = {
        "entry.1797301416": "Welrikyson Felix",
        "entry.1166974658": "Bike",
        "entry.1065046570": "Moderado",
        "entry.885711731_hour": hour,
        "entry.885711731_minute": minutes,
        "entry.885711731_second": seconds,
    }
    response = requests.get(url=url, params=params)
    print(response)