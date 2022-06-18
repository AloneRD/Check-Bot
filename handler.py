import logging
import telegram
import os
from dotenv import load_dotenv


class TelegramLogsHandler(logging.Handler):

    def __init__(self) -> None:
        super().__init__()
        load_dotenv()
        token = os.getenv("TELEGRAM_TOKEN")
        self.bot = telegram.Bot(token)
        self.chat_id = os.environ.get("TG_CHAT_ID")

    def emit(self, record) -> None:
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)
