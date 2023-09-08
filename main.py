from fastapi import FastAPI, Query
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class UserInfo(BaseModel):
    slack_name: str
    track: str

@app.get('/api')
async def get_info(slack_name: str = Query(..., description="Your Slack name"), track: str = Query(..., description="Your track (e.g., backend)")):
    # Get the current day of the week
    current_day = datetime.now().strftime('%A')

    # Get the current UTC time in ISO 8601 format
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Assuming these URLs need to be dynamic based on the input
    github_file_url = f"https://github.com/Reganmatics/HNG/blob/main/main.py"
    github_repo_url = f"https://github.com/Reganmatics/HNG"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return response_data

