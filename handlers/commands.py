from telegram import Update
from telegram.ext import CallbackContext
from keyboards import inlines, replies
from translation import get_translation as _

def start(update: Update, context: CallbackContext):     
    language = context.user_data.get("language", None)
    if not language:
        context.user_data["language"] = "uz"
    update.message.reply_text(_("bot salom", language), reply_markup=replies.get_main(language))
    
def help(update: Update, context: CallbackContext):
    update.message.reply_text("Sizga qanday yordam bera olaman")

def contact(update: Update, context: CallbackContext):
    update.message.reply_text("Murojaat uchun +123456789")

def language(update: Update, context: CallbackContext):
    update.message.reply_text("Tilni tanlang", reply_markup=inlines.get_language())
    