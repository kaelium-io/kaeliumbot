import json
import os
import telebot
from telebot.types import Update, Message


bot = telebot.TeleBot(os.environ["BOT_TOKEN"], threaded=False)


@bot.message_handler(commands=["start"])
def send_welcome(message: Message):
    bot.reply_to(message, "Howdy, how are you doing?")


def handler(event, context):
    if not (update := Update.de_json(json.loads(event["body"]))):
        return
    bot.process_new_updates([update])
