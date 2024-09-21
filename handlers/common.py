from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from translation import get_translation as _
from python_db import BOOKS
from keyboards import replies, inlines
import states

def get_language(update: Update, context: CallbackContext):
    context.user_data["language"] = update.callback_query.data
    update.callback_query.answer()
    update.callback_query.message.delete()
    update.callback_query.message.reply_text(_("change language", update.callback_query.data))
    
def get_books(update: Update, context: CallbackContext):
    language = context.user_data["language"]
    books = ""   
    book_list = [] 
    for book in BOOKS:
        if book["_type"] == "paper":
            book_list.append(book)
            books += "==================\n"
            books += f"Nomi: {book['title']}\n"            
            books += f"Narxi: {book['price']}\n" 
            books += "==================\n\n"           
    if not books:
        update.message.reply_text(_('No paper books found', language), reply_markup=replies.get_main(language))
        return
    
    message = "<b>Kitoblar:</b>\n" + books
    if update and update.message:
        update.message.reply_text(message, reply_markup=inlines.get_list_button(book_list), parse_mode="html")
    if update and update.callback_query:
        update.callback_query.message.reply_text(message, reply_markup=inlines.get_list_button(book_list), parse_mode="html")
    return states.BOOK_SINGLE

def get_book(update: Update, context: CallbackContext):
    print("DATA", update.callback_query.data)
    book_id = int(update.callback_query.data.split("-")[-1])
    update.callback_query.answer()
    update.callback_query.message.delete()
    
    book = None
    
    for item in BOOKS:
        if item['id'] == book_id:
            book = item
            break
    
    if not book:
        update.callback_query.message.reply_text("Siz izlagan kitob topilmadi")
        return get_books(update, context) 
    
    context.user_data["selected_book"] = book_id 

    caption = f"<b>{book['title']}</b>\n"
    caption += f"<b>Narxi: </b>{book['price']}\n"
    caption += f"<b>Tavsif: </b>{book['description']}\n"
    
    update.callback_query.message.reply_photo(photo=book['cover'], caption=caption, parse_mode="html", reply_markup=inlines.get_book_actions())
    return states.BOOK_ACTION


def get_book_action(update: Update, context: CallbackContext):
    data = update.callback_query.data
    update.callback_query.answer()
    update.callback_query.message.delete()
    
    if data == "cancel":
        return get_books(update, context)
    else:
        update.callback_query.message.reply_text("Buyurtma sonini kiriting: ")
        return states.GET_ORDER
    
def get_book_order(update: Update, context: CallbackContext):
    amount = update.message.text
    
    try:
        amount = int(amount)
    
    except:
        update.message.reply_text("Buyurtma sonini raqamlarda kiriting: ")
        return states.GET_ORDER
    
    order_item = {
        "book_id": context.user_data["selected_book"],
        "amount": amount
    }
    
    korzina = context.user_data.get("korzina", None)
    if korzina:
        korzina.append(order_item)
        context.user_data['korzina'] = korzina
    else:
        context.user_data['korzina'] = [order_item]
        
    update.message.reply_text("Sizning buyurtmangiz savatga qo'shildi ", reply_markup=replies.get_main("uz"))
    return states.END