import json
import os
import time
from typing import NoReturn
import requests
import telegram
from dotenv import load_dotenv
import logging

logger = logging.getLogger("CheckBot")
logger.setLevel(logging.INFO)


def main():
    load_dotenv()
    auth_token_api = os.getenv("AUTH_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")
    token = os.getenv("TELEGRAM_TOKEN")

    logger.info("Бот запущен")

    get_checks(auth_token_api, chat_id, token)


def get_checks(auth_token_api: str, chat_id: str, token: str) -> NoReturn:
    url_api = "https://dvmn.org/api/long_polling/"
    headers = {
        "Authorization": f"Token {auth_token_api}"
        }
    timestamp = time.time()
    while True:
        try:
            response_tasks = requests.get(url_api, headers=headers, params=str(timestamp), timeout=20)
            response_tasks.raise_for_status()
            review_info = response_tasks.json()
            if review_info['status'] == "timeout":
                timestamp = review_info['timestamp_to_request']
            else:
                timestamp = review_info["last_attempt_timestamp"]
                send_message_telegramm(review_info, chat_id, token) 
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            time.sleep(5)


def send_message_telegramm(task: json, chat_id: str, token: str) -> NoReturn:
    bot = telegram.Bot(token)

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
        bot.send_message(chat_id=chat_id, text=text_message)


if __name__ == "__main__":
    main()
