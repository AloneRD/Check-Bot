# Check Bot

Данный бот предназначен для уведомлений пользователей о статусе проверки домашнего задания на образовательной платформе devman
## Запуск бота локально
Для запуска бота на вашем сервере необходимо выполнить следующие действия:

1. Cоздать бота в Телеграмм  [см.тут](https://core.telegram.org/bots).
2. Инициализировать с вашим ботом чат.
3. Склонировать себе файлы репозитория выполнив команду **git clone https://github.com/AloneRD/Check-Bot.git**.
4. Установить необходимы зависимости **pip install -r requirements.txt**.
5. В директории с проектом создать файл **.env** со следующим содержимом:
 ```
    AUTH_TOKEN="cdfgdf0fae33ef2e587da8bd2550e"
    TELEGRAM_TOKEN="53f5467:AAHamFQOxdssdBci_scJkFbfdfgdHxJ6cUvo_81El5Yc"
 ```
   - **AUTH_TOKEN** личный токен для доступа к API сайта devman.org
   - **TELEGRAM_TOKEN** токен к вашему телеграмм боту
6. задать переменную окружения **TG_CHAT_ID** со значением вашего chat_id [см.тут](https://perfluence.net/blog/article/kak-uznat-id-telegram)
7. запустить бота **.\CheckBot.py**

## Запуск бота в Docker контейнере
1. Cоздать бота в Телеграмм  [см.тут](https://core.telegram.org/bots).
2. Инициализировать с вашим ботом чат.
3. Склонировать себе файлы репозитория выполнив команду **git clone https://github.com/AloneRD/Check-Bot.git**.
4. Установить докер к себе на компьютер.
5. В директории с проектом создать файл **.env** со следующим содержимом:
 ```
    AUTH_TOKEN=cdfgdf0fae33ef2e587da8bd2550e
    TELEGRAM_TOKEN=53f5467:AAHamFQOxdssdBci_scJkFbfdfgdHxJ6cUvo_81El5Yc
    TG_CHAT_ID=000000
 ```
 6. Выполнить сборку docker контейнера.
 ```
    docker build -t  check_bot .
 ```
 7. Запустить контейнер командой
 ```
    docker run --env-file .env -dp 3000:3000 check_bot
 ```
