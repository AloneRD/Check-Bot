import os
import time
from typing import NoReturn
import requests

TOKEN = os.environ.get("TOKEN")


def get_checks() -> NoReturn:
    url = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {TOKEN}"
        }
    timestamp = time.time()
    while True:
        print(timestamp)
        try:
            request = requests.get(url, headers=headers, params=str(timestamp))
            request.raise_for_status()
            request = request.json()
            if request['status'] == "timeout":
                timestamp = request['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            print("Timeout exceeded")
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        print(request)


get_checks()
