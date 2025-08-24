import telebot
import sqlite3


API_TOKEN = "8341067903:AAE33Q1Q5FAXJPL2NFcsvz55OE-VPP0rUcA"

connect = sqlite3.connect("email.db", check_same_thread=False)
data = connect.cursor()
data.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, email TEXT)")
connect.commit()


bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am the Mail-Checker Bot! You can add a email and I can to check if anyone has written to you. Use /help to see the commands.")

@bot.message_handler(commands=['setemail'])
def ask_email(message):
    bot.reply_to(message, "Write your email.")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Choose another variant to ask.")



bot.infinity_polling()