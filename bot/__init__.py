
from pyrogram import Client,filters
from .config import Config
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)



delall = "/delall"
del_count = "oh"
del_count_edit = "oh-"


@bot.on_message()
def bot(client, message):
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





