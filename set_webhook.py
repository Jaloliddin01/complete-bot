from telegram import Bot
import os

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)

bot.set_webhook('https://vertow.pythonanywhere.com/')
print(bot.get_webhook_info())