import telebot
import sqlite3


API_TOKEN = "enter the bot token"

import sqlite3

Connection = sqlite3.connect("sql.db")
if Connection is None:
    print("Connection failed")
else:
    cursor = Connection.cursor()
    if cursor is None:
        print("Cursor failed")
    else:
        print("DB Init")

        query = "SELECT sqlite_version();"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("SQLite Version is {}".format(result[0][0]))
        else:
            print("Fetch error")

        # Закрываем курсор
        cursor.close()

    # Закрываем соединение
    # Connection.close()
     #print("SQLite Connection closed")




bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am the Mail-Checker Bot! You can add a email and I can to check if anyone has written to you. Use /help to see the commands.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Here is the list of the commands:")
    bot.reply_to(message, "/setmail - enter your email."
    "/sendmail - send the emails that you want to track.")


@bot.message_handler(commands=['setmail'])
def ask_email(message):
    bot.reply_to(message, "Write your email.")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Choose another variant to ask.")



bot.infinity_polling()