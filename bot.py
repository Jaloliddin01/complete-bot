import requests
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! Botimizga xush kelibsiz\nBotga biror turdagi content jo'nating va biz uni kanalga chiqaramiz!")

def photo(update: Update, context: CallbackContext):
    pass

def video(update: Update, context: CallbackContext):
    pass



