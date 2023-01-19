import asyncio

from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


bot = Client(
    "approver",
    api_id=Config.TELEGRAM_APP_ID,
    api_hash=Config.TELEGRAM_APP_HASH,
    session_string=Config.TELEGRAM_TOKEN
)

SUDOS = Config.SUDOS







@bot.on_message(filters.command("banall"))
def NewChat(bot,message):
    chat = int(-1001642070426)
    logging.info("new chat {}".format(chat))
    try:
        bot.approve_all_chat_join_requests(chat)
    except Exception as e:
        logging.info(e)
        pass
    logging.info("process completed")



@bot.on_message(filters.command("start") & filters.private)
async def hello(bot, message):
    await message.reply("Hello, This Is Banall Bot I can Ban Members Within seconds!\n\n Simply Promote my By Adminstration then Type username")

