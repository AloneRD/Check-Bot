#Check Bot
Данный бот предназначен для уведомлений пользователей о статусе проверки домашнего задания на образовательной платформе devman
##Запуск бота
Для запуска бота на вашем сервере необходимо выполнить следующие действия:

1. создать бота в Телеграмм  [см.тут](https://core.telegram.org/bots)
2. инициализировать с вашим ботом чат
3. склонировать себе файлы репозитория выполнив команду **git clone https://github.com/AloneRD/Check-Bot.git**
4. установить необходимы зависимости **pip install -r requirements.txt**
5. в директории с проектом создать файл **.env** со следуюющим содержимом
    AUTH_TOKEN="cdfgdf0fae33ef2e587da8bd2550e"
    TELEGRAM_TOKEN="53f5467:AAHamFQOxdssdBci_scJkFbfdfgdHxJ6cUvo_81El5Yc"
   - **AUTH_TOKEN** личный токен для доступа к API сайта devman.org
   - **TELEGRAM_TOKEN** токен к вашему телеграмм боту
6. задать переменную окружения **CHAT_ID** со значением вашего CHAT_ID [см.тут](https://perfluence.net/blog/article/kak-uznat-id-telegram)
7. запустить бота **.\CheckBot.py**
