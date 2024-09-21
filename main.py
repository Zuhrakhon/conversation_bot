from flask import Flask, request
from telegram import Update 
from dispatcher import dispatcher, bot

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def get_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    print(vars(update.callback_query) if update.callback_query else 0)
    dispatcher.process_update(update)
    return {"result": "ok"}


