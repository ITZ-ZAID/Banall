from pyrogram import idle
from .config import Config
from . import bot, ass
bot.start()
if Config.PYRO_SESSION:
   ass.start()
idle()
bot.stop()
