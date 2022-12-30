#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#

import os

import logging

logging.basicConfig(

    level=logging.INFO,

    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",

    datefmt='%d-%b-%y %H:%M:%S',

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2055718473:AAHGch-ioqCoYkzTkMtw0SDG1UkYK91IQWc")

    # Get from my.telegram.org

    APP_ID = int(os.environ.get("APP_ID", "8281168"))

    # Get from my.telegram.org

    API_HASH = os.environ.get("API_HASH", "445ff67ec34858448ac184c7479ce917")

    # Generate a user session string

    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BQANOTEuMTA4LjU2LjEzMAG7g2FgIDFGJidbjiqfYwzDZss6fXeQG9iyGZfDmROQnAg1wMXp/lwPtzje/2bP5T2+9dLeTbHA/xBVKIybmdjE3jBaoUiu+IyMFQjS7Yl0opr5XvYlhVTKK2wWPHiuJuDYWFXjLrpjAVDjWezj9vHJL7fPVvMbNyQqlWKY3r18nyD+7+C3Z7VcNhGUupgD8eM/GBoNDxFPtEBI/PIiBashYOanBBoQWrj6YXevQFWqcTZeekH5tTRx81k37tQrd8F2MwzMiFUEUHFda8XZtuRhZvsyQ6sgaSPLeJUg9jLIase/5GR5xF0x/92eVsXsypyoFNuCvvWyi8uXy6D5SNbvrw==")

    # Database URI

    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://123:123@cluster0.fr6gfgg.mongodb.net/?retryWrites=true&w=majority")

def LOGGER(name: str) -> logging.Logger:

    return logging.getLogger(name)
