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

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)
TG_MAX_SEL_MESG = 99
TG_MIN_SEL_MESG = 0

from typing import List


async def mass_delete_messages(
    client: bot,
    chat_id: int,
    message_ids: List[int]
):
    return await client.delete_messages(
        chat_id=chat_id,
        message_ids=message_ids,
        revoke=True
    )

async def get_messages(
    client: bot,
    chat_id: int,
    min_message_id: int,
    max_message_id: int,
    filter_type_s: List[str]
):
    messages_to_delete = []
    async for msg in bot.get_chat_history_count(
        chat_id=chat_id,
        limit=None
    ):
        if (
            min_message_id <= msg.message_id and
            max_message_id >= msg.message_id
        ):
            if len(filter_type_s) > 0:
                for filter_type in filter_type_s:
                    obj = getattr(msg, filter_type)
                    if obj:
                        messages_to_delete.append(msg.message_id)
            else:
                messages_to_delete.append(msg.message_id)
        # append to the list, based on the condition
        if len(messages_to_delete) > TG_MAX_SEL_MESG:
            await mass_delete_messages(
                client,
                chat_id,
                messages_to_delete
            )
            messages_to_delete = []
    # i don't know if there's a better way to delete messages
    if len(messages_to_delete) > TG_MIN_SEL_MESG:
        await mass_delete_messages(
            client,
            chat_id,
            messages_to_delete
        )
        messages_to_delete = []









@bot.on_message(filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            zaid = msg.reply('Starting Banning in Chat')
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            zaid.edit("Banned Total {}".format(count_kicks))
        except Exception as e:
            zaid.edit('failed to kicked {}'.format(str(e)))
    else:
        zaid.edit("i need to be admin In This Group To Perform This Action!")




@bot.on_message(filters.command("start") & filters.private)
async def hello(bot, message):
    await message.reply("Hello, This Is Banall Bot I can Ban Members Within seconds!\n\n Simply Promote my By Adminstration then Type username")




@bot.on_message(
    filters.command('delall'))
async def delall(client: bot, message: Message):
    try:
        status_message = await message.reply_text("Processing")
    except ChatAdminRequired:
        status_message = None

    await get_messages(
        client,
        message.chat.id,
        0,
        status_message.message_id if status_message else message.message_id,
        []
    )
