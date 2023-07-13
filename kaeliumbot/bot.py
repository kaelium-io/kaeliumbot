import telebot
from telebot.types import Message


bot = telebot.TeleBot(token="", threaded=False)


@bot.message_handler(commands=["start"])
def send_welcome(message: Message):
    bot.reply_to(message, "Howdy, how are you doing?")
