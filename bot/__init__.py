import asyncio

from pyrogram import Client,filters
from .config import Config
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)



@bot.on_message(filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply('new Chat{}'.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply("Banned {}".format(count_kicks))
        except Exception as e:
            msg.reply('failed to kicked {}'.format(str(e)))
    else:
        msg.reply("i need to be admin In This Group To Perform This Action!")




@bot.on_message(filters.command("start") & filters.private)
async def hello(bot, message):
    await message.reply("Hello, This Is Banall Bot I can Ban Members Within seconds!\n\n Simply Promote my By Adminstration then Type username")




delall = "/delall"
del_count = "oh"
del_count_edit = "oh-"

@bot.on_message(filters.command("delall"))
async def delall(client, message):
    print(message)
    if message["text"] is not None:
        if message["from_user"]["is_self"] and message["text"] == delall:
            chat_id = message["chat"]["id"]
            msgs_list = Client.get_history(chat_id=chat_id, self=app)
            ids_list = []
            for i in msgs_list:
                if i["chat"]["id"] == chat_id and i["from_user"]["is_self"]:
                    ids_list.append(i["message_id"])
            Client.delete_messages(chat_id=chat_id, message_ids=ids_list, self=app)

        if message["from_user"]["is_self"] and message["text"].lower().startswith(del_count):
            count = 0
            if (message["text"])[2:].isdigit():
                count = int((message["text"])[2:])+1
            elif message["text"].lower() == del_count:
                count = 2
            if count > 0:
                chat_id = message["chat"]["id"]
                msgs_list = Client.get_history(chat_id=chat_id, self=app)
                ids_list = []
                for i in range(0, len(msgs_list)):
                    if msgs_list[i]["chat"]["id"] == chat_id and msgs_list[i]["from_user"]["is_self"]:
                        ids_list.append(msgs_list[i]["message_id"])
                        if len(ids_list) == count: break
                Client.delete_messages(chat_id=chat_id, message_ids=ids_list, self=app)

        if message["from_user"]["is_self"] and message["text"].lower().startswith(del_count_edit):
            count = 0
            if (message["text"])[3:].isdigit():
                count = int((message["text"])[3:])+1
            elif message["text"].lower() == del_count_edit:
                count = 2
            if count > 0:
                chat_id = message["chat"]["id"]
                msgs_list = Client.get_history(chat_id=chat_id, self=app, limit=count)
                ids_list = []
                for i in range(0, len(msgs_list)):
                    if msgs_list[i]["chat"]["id"] == chat_id and msgs_list[i]["from_user"]["is_self"]:
                        ids_list.append(msgs_list[i]["message_id"])
                        app.edit_message_text(chat_id=chat_id, message_id=msgs_list[i]["message_id"], text="[DELETED]")
                        if len(ids_list) == count: break
                Client.delete_messages(chat_id=chat_id, message_ids=ids_list, self=app)




