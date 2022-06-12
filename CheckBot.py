import json
import os
import time
from typing import NoReturn
import requests
import telegram
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = telegram.Bot("5358565467:AAHamFQOxdBci_scJkFHxJ6cUvo_81El5Yc")


def get_checks() -> NoReturn:
    url = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {TOKEN}"
        }
    timestamp = time.time()
    while True:
        try:
            request = requests.get(url, headers=headers, params=str(timestamp))
            request.raise_for_status()
            request = request.json()
            if request['status'] == "timeout":
                timestamp = request['timestamp_to_request']
            else:
                send_message_telegramm(request)
        except requests.exceptions.ReadTimeout:
            print("Timeout exceeded")
        except requests.exceptions.ConnectionError:
            print("Connection Error")


def send_message_telegramm(task: json) -> NoReturn:
    tasks = task['new_attempts']
    for task in tasks:
        lesson_title = task['lesson_title']
        lesson_url = task['lesson_url']
        result = task['is_negative']
        if result is True:
            text_message = f"У Вас проверили работу {lesson_title}.\n\r\
                             Ссылка на работу {lesson_url}.\n\r\
                             К сожалению в работе нашлись ошибки."
        else:
            text_message = f"У Вас проверили работу {lesson_title}.\n\r\
                             Ссылка на работу {lesson_url}\n\r\
                             Преподователю все понравилось!"
        bot.send_message(chat_id=937205408, text=text_message)


get_checks()
