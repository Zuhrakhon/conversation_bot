telegram_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    
    print(telegram_id, first_name, last_name)
    
    try:
        conn = sqlite3.connect("my_bot.db")
        cursor = conn.cursor()
        
        cursor.execute(
            f"""
            INSERT INTO telegram_users (telegram_id, first_name, last_name) VALUES ('{telegram_id}', '{first_name}', '{last_name}')
            """
        )
    
    except sqlite3.IntegrityError:
        pass
    
    conn.commit()
    conn.close()
    
    
def register(update: Update, context: CallbackContext):
    update.message.reply_text("Royxatdan o'tish uchun ism-familiyangizni kiriting: ")
    return states.FULLNAME


def get_users(update: Update, context: CallbackContext):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM telegram_users")
    users = cursor.fetchall()
    
    conn.close()
    
    update.message.reply_text("Royxatdan o'tganlar:")
    for user in users:
        update.message.reply_text(f"ID: {user[0]}, Ism: {user[1]}, Familya: {user[2]}")