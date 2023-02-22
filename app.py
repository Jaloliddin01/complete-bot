from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import MessageHandler, CommandHandler, Filters, Dispatcher
import os

from bot import (
    start,
    photo,
    video,
)

app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "GET":
        return "Get method"
    elif request.method == "POST":

        data = request.get_json(force=True)
        update = Update.de_json(data, bot)

        db = Dispatcher(bot, update)

        db.add_handler(CommandHandler('start', start))
        db.add_handler(MessageHandler(Filters.photo, photo))
        db.add_handler(MessageHandler(Filters.video, video))

        db.process_update(update)
        return 'OK'

if __name__ == "__main__":
    main()
