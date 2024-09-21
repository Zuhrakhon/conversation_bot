from telegram import ReplyKeyboardMarkup, KeyboardButton
from translation import get_translation as _

def get_contact():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)]
        ], resize_keyboard=True
    )
    
def get_location():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Manzilni yuborish", request_location=True)]
        ], resize_keyboard=True
    )
    
def get_main(lang):
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(_("books", lang)), KeyboardButton(_("audio books", lang))],
            [KeyboardButton(_("korzina", lang)), KeyboardButton(_("languaage", lang)),]
        ], resize_keyboard=True
    )
    
def get_finish_order():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Buyurtmani tugatish"), KeyboardButton("Savatni tozalash")]
        ], resize_keyboard=True
    )

