import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
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

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)

CHAT = int(-1001883645971)

@bot.on_message(filters.command("banall"))
async def _(bot, msg):
    print("getting memebers from {}".format(CHAT))
    async for i in bot.iter_chat_members(CHAT):
        try:
            await bot.ban_chat_member(chat_id =CHAT,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,CHAT))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")
