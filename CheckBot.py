import json
import os
import time
from typing import NoReturn
import requests
import telegram
from dotenv import load_dotenv


def get_checks() -> NoReturn:
    AUTH_TOKEN_API = os.getenv("AUTH_TOKEN")

    url_api = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {AUTH_TOKEN_API}"
        }
    timestamp = time.time()
    while True:
        try:
            response_tasks = requests.get(url_api, headers=headers, params=str(timestamp), timeout=20)
            response_tasks.raise_for_status()
            response_tasks = response_tasks.json()
            if response_tasks['status'] == "timeout":
                timestamp = response_tasks['timestamp_to_request']
            else:
                timestamp = time.time()
                send_message_telegramm(response_tasks)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            time.sleep(5)


def send_message_telegramm(task: json) -> NoReturn:
    CHAT_ID = os.environ.get("TG_CHAT_ID")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    bot = telegram.Bot(TELEGRAM_TOKEN)

    tasks = task['new_attempts']
    for task in tasks:
        lesson_title = task['lesson_title']
        lesson_url = task['lesson_url']
        result = task['is_negative']
        if result:
            text_message = f"У Вас проверили работу {lesson_title}.\n\r\
                             Ссылка на работу {lesson_url}.\n\r\
                             К сожалению в работе нашлись ошибки."
        else:
            text_message = f"У Вас проверили работу {lesson_title}.\n\r\
                             Ссылка на работу {lesson_url}\n\r\
                             Преподователю все понравилось!"
        bot.send_message(chat_id=CHAT_ID, text=text_message)


if __name__ == "__main__":
    load_dotenv()
    get_checks()
