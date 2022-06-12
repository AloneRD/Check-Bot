import os
from typing import NoReturn
import requests

TOKEN = os.environ.get("TOKEN")


def get_checks() -> NoReturn:
    request=requests.get("") 
    