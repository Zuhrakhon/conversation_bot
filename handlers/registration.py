from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
import states
from keyboards import replies
import constanta
    
def get_fullname(update: Update, context: CallbackContext):
    if update.message and not update.message.text:
        update.message.reply_text("Iltimos, ismingizni matn ko'rinishida kiriting")
        return states.FULLNAME
    
    full_name = update.message.text
    context.user_data["fullname"] = full_name
    
    update.message.reply_text("Yoshingizni kiriting: ")
    return states.AGE

def get_age(update: Update, context: CallbackContext):
    if update.message and not update.message.text:
        update.message.reply_text("Iltimos, yoshingizni matn ko'rinishida kiriting")
        return states.AGE
    
    age = update.message.text
    
    if not str(age).isdigit():
        update.message.reply_text("Yoshingizni raqamlar bilan yozing")
        return states.AGE
    
    context.user_data["age"] = age
    update.message.reply_text("Telefon raqamingizni 'Telefon raqamni yuborish' tugmasi orqali yuboring: ", reply_markup=replies.get_contact() )
    return states.CONTACT

def get_contact(update: Update, context: CallbackContext):
    if update.message and not update.message.contact:
        update.message.reply_text("Iltimos, raqamingizni matn ko'rinishida kiriting")
        return states.CONTACT
    
    phone = update.message.contact.phone_number
    context.user_data["phone"] = phone
    update.message.reply_text("Yashash manzilingizni yuboring: ", reply_markup=replies.get_location())
    return states.LOCATION

def get_location(update: Update, context: CallbackContext):
    if update.message and not update.message.location:
        update.message.reply_text("Manzilingizni kiritish uchun 'Manzilni yuborish' tugmasini bosing: ")
        return states.LOCATION
    
    context.user_data["location"] = {
        "longitude": update.message.location.longitude,
        "latidute": update.message.location.latitude
    }
    
    message = "<b>Yangi foydalanuvchi</b>\n"
    message += f"Name: {context.user_data['fullname']}\n"
    message += f"Age: {context.user_data['age']}\n"
    message += f"Phone: {context.user_data['phone']}\n"
    
    for admin in constanta.ADMIN:
        context.bot.send_message(admin, message, "html")
    
    update.message.reply_text("Tabriklayman! Muvaffaqiyatli ro'yxatdan o'tdingiz", reply_markup=ReplyKeyboardRemove())
    return states.END