import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = '6218848472:AAF2zENlm8teqYnbK4OPgSXcGmOCBI0Cd5I'#os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! Botimizga xush kelibsiz\nBotga biror turdagi content jo'nating va biz uni kanalga chiqaramiz!")

def add_photo(update: Update, context: CallbackContext):
    photo_id = update.message.photo[-1].file_id
    r = requests.post('https://djdev001.pythonanywhere.com/api/add-img/', json={"photo_id": photo_id})

    data = r.json()
    doc_id = data.get("doc_id")
    if doc_id:
        bot = context.bot
        btns = [
            [
                InlineKeyboardButton(text=f"👍 {0}", callback_data=f"like:{doc_id}"),
                InlineKeyboardButton(text=f"👎🏿 {0}", callback_data=f"dislike:{doc_id}"),
            ]
        ]
        bot.send_photo(
            chat_id="@testadsme", 
            photo=photo_id, 
            reply_markup=InlineKeyboardMarkup(inline_keyboard=btns)
        )

# def video(update: Update, context: CallbackContext):
#     pass

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.photo, add_photo))

    updater.start_polling()

if __name__ == "__main__":
    main()



