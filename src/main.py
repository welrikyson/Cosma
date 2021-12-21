import datetime
import webbrowser

from src.notify_activity import notify_activity
from src.services import activity_service, token_service
from typing import Optional
from fastapi import FastAPI, Query, responses

from src.authentication.token import load_token, save_token
from src.globals import Globals

app = FastAPI()


def init_notification():
    activities_of_today = activity_service.get_in_today(load_token())
    total = 0
    for activity in activities_of_today:
        notify_activity(activity)
        isodate = activity["start_date"]
        last_date = datetime.datetime.strptime(isodate, "%Y-%m-%dT%H:%M:%SZ")
        Globals.set_last_activity_date_notify(last_date)
        total += 1

    return total


@app.get("/", response_class=responses.HTMLResponse)
async def root():
    token = load_token()
    if token is None:
        return responses.RedirectResponse(
            url="https://www.strava.com/oauth/authorize?"
                "client_id=75467&response_type=code&"
                "redirect_uri=https://cosma-croqh.ondigitalocean.app/auth&"
                "approval_prompt=force&"
                "scope=activity:read")
    else:
        with open("src/views/home.html", "r", encoding='utf-8') as f:
            home_html = f.read()
        return home_html


@app.get("/notify")
async def notify():
    total_activities_sync = init_notification()
    return total_activities_sync


@app.get("/auth", response_class=responses.HTMLResponse)
async def root(code: Optional[str] = Query(None)):
    token = token_service.get_token(code)
    save_token(token)
    return responses.RedirectResponse("https://cosma-croqh.ondigitalocean.app/")
