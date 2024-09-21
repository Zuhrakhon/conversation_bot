from telegram import Update
from telegram.ext import CallbackContext
from python_db import get_book_id
from keyboards import inlines, replies
import constanta, states

def view_korzina(update: Update, context: CallbackContext):
    korzina_items = context.user_data.get('korzina', [])
    if not korzina_items:
        update.message.reply_text("You haven't got any books in your cart")
        return states.END
    
    message = "Kitoblar\n"
    total_amount = 0
    items_for_buttons = []
    
    for item in korzina_items:
        book = get_book_id(item['book_id'])
        if book:
            item['title'] = book['title']
            items_for_buttons.append(item)
            total_amount += book['price'] * item['amount']
            message += f"Kitob: {book['title']} \n"
            message += f"Narxi: {book['price']} \n"
            message += f"Soni: {item['amount']} \n"
            message += f"Umumiy summa: {book['price'] * item['amount']} \n"
            message += "******************\n\n "
            
    message += f"Jami summa: {total_amount}"
    
    update.message.reply_text(message, reply_markup=inlines.change_order_counts(items_for_buttons))
    return states.CART_ACTIONS
    
def korzina_action(update: Update, context: CallbackContext):
    data = update.callback_query.data
    
    if data == "complete-order":
        update.callback_query.answer()
        korzina_items = context.user_data['korzina']
        message = "Buyurtma\n"
        full_name = str(update.callback_query.from_user.first_name) + " " + str(update.callback_query.from_user.last_name)
        message += f"Mijoz: {full_name}\n\n"
        message = "Kitoblar\n"
        total_amount = 0        
        for item in korzina_items:
            book = get_book_id(item['book_id'])
            if book:
                item['title'] = book['title']
                total_amount += book['price'] * item['amount']
                message += f"Kitob: {book['title']} \n"
                message += f"Narxi: {book['price']} \n"
                message += f"Soni: {item['amount']} \n"
                message += f"Umumiy summa: {book['price'] * item['amount']} \n"
                message += "******************\n\n "
        message += f"Jami summa: {total_amount}"
        
        for admin in constanta.ADMIN:
            context.bot.send_message(admin, message)
        update.callback_query.message.delete()
        context.user_data['korzina'] = []
        update.callback_query.message.reply_text("Buyurtmalaringiz adminga yuborildi", reply_markup=replies.get_main("uz"))
        return states.END
    
    elif data == "clear-cart":
        update.callback_query.answer()
        update.callback_query.message.delete()
        context.user_data['korzina'] = []
        update.callback_query.message.reply_text("Savatcha bo'shatildi", reply_markup=replies.get_main("uz"))
        return states.END
    
    else:
        action, book_id = data.split("-")
        book_id = int(book_id)
        korzina_items = context.user_data['korzina']
        
        if action == "default":
            book = get_book_id(book_id)
            update.callback_query.answer(book['title'])
            return states.CART_ACTIONS
        
        elif action == "increase":
            new_korzina_items = []
            
            for item in korzina_items:
                if item['book_id'] == book_id:
                    item['amount'] = item['amount'] + 1
                    
                new_korzina_items.append(item)
            
            context.user_data['korzina'] = new_korzina_items
        
        elif action == "decrease":
            new_korzina_items = []
            
            for item in korzina_items:
                if item['book_id'] == book_id:
                    item['amount'] = item['amount'] - 1
                    
                if item['amount'] > 0:
                    new_korzina_items.append(item)
            
            context.user_data['korzina'] = new_korzina_items
        
        elif action == "clear":
            new_korzina_items = []
            
            for item in korzina_items:
                if item['book_id'] != book_id:
                    new_korzina_items.append(item)
            
            context.user_data['korzina'] = new_korzina_items
        
        update.callback_query.answer()
        items_for_buttons = []
        total_amount = 0
        message = "Kitoblar\n"
        for item in context.user_data['korzina']:
            book = get_book_id(item['book_id'])
            if book:
                item['title'] = book['title']
                items_for_buttons.append(item)
                total_amount += book['price'] * item['amount']
                message += f"Kitob: {book['title']} \n"
                message += f"Narxi: {book['price']} \n"
                message += f"Soni: {item['amount']} \n"
                message += f"Umumiy summa: {book['price'] * item['amount']} \n"
                message += "******************\n\n "
        message += f"Jami summa: {total_amount}"
        update.callback_query.message.delete()
        update.callback_query.message.reply_text(message, reply_markup=inlines.change_order_counts(items_for_buttons))
        return states.CART_ACTIONS