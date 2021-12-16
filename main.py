import datetime
import webbrowser

from Globals import Globals
from NotifyActivity import notify_activity
from Services import TokenService, ActivityService
from typing import Optional
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse

from authentication.token import load_token, save_token
from views import SucessPage

app = FastAPI()


def init_notification():
    activities_of_today = ActivityService.get_in_today(load_token())
    total = 0
    for activity in activities_of_today:
        notify_activity(activity)
        isodate = activity["start_date"]
        last_date = datetime.datetime.strptime(isodate, "%Y-%m-%dT%H:%M:%SZ")
        Globals.set_last_activity_date_notify(last_date)
        total = total + 1

    return total


@app.get("/", response_class=HTMLResponse)
async def root():
    token = load_token()
    if token is None:
        return RedirectResponse(
            url="https://www.strava.com/oauth/authorize?"
                "client_id=75467&response_type=code&"
                "redirect_uri=http://localhost:8000/auth&"
                "approval_prompt=force&"
                "scope=activity:read")
    else:
        total_activities_sync = init_notification()
        return SucessPage.success_page(total_activities_sync)
        

@app.get("/auth", response_class=HTMLResponse)
async def root(code: Optional[str] = Query(None)):
    token = TokenService.get_token(code)
    save_token(token)

    return RedirectResponse("http://localhost:8000")

webbrowser.open("http://localhost:8000")
