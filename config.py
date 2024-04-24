import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token from discord.com/developers/applications
DC_BOT_TOKEN = os.environ.get("DC_BOT_TOKEN", "")

#Port
PORT = os.environ.get("PORT", "8080")

#Command prifix
PRIFIX = os.environ.get("PRIFIX", "!")

LOG_FILE = "bot-log-info.txt"

os.remove(LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("discord").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
