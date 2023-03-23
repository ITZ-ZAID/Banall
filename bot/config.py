import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", None)
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH']
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID'])
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
