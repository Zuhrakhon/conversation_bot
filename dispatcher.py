from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import commands, registration, common, korzina
import states

bot = Bot(token="7340221507:AAEq-yqi9XBat1Wxkrpd2KLIsw2fRlku1YA")

dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(CommandHandler("start", commands.start))
dispatcher.add_handler(CommandHandler("help", commands.help))
dispatcher.add_handler(CommandHandler("contact", commands.contact))
dispatcher.add_handler(CommandHandler("language", commands.language))
dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            MessageHandler(Filters.text("korzina"), korzina.view_korzina)
        ],
        states={
            states.CART_ACTIONS: [
                CallbackQueryHandler(korzina.korzina_action)
            ]
        },
        fallbacks=[
            CommandHandler("start", commands.start)
        ]
    )
)


dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            MessageHandler(Filters.text("📕 Kitoblar"), common.get_books),
            MessageHandler(Filters.text("📕 Книги"), common.get_books),
            MessageHandler(Filters.text("📕 Books"), common.get_books)
        ],
        states={
            states.BOOK_SINGLE: [
                CallbackQueryHandler(common.get_book)
            ],
            states.BOOK_ACTION: [
                CallbackQueryHandler(common.get_book_action)
            ],
            states.GET_ORDER: [
                MessageHandler(Filters.text, common.get_book_order)
            ]
        },
        fallbacks=[
            CommandHandler("start", commands.start)
        ]
    )
)


dispatcher.add_handler(CallbackQueryHandler(common.get_language))