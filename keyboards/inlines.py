from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_language():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="O'zbek tili", callback_data="uz")
            ],
            [
                InlineKeyboardButton(text="English", callback_data="en")
            ],
            [
                InlineKeyboardButton(text="Rus tili", callback_data="ru")
            ],
            [
                InlineKeyboardButton(text="Kun uz", url="https://kun.uz")
            ]
        ], resize_keyboard=True
    )
    
def get_list_button(items):
    keyboards = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=item['title'], callback_data=f"book-{item['id']}")] for item in items 
        ]
    )
    print(keyboards)
    return keyboards
    
def get_book_actions():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Orta qaytish", callback_data="cancel"), InlineKeyboardButton("Buyurtma berish", callback_data="order")
            ]
        ]
    )
    
def change_order_counts(items):
    keyboards = []
    for item in items:
        keyboards.append(
            [
                InlineKeyboardButton("+", callback_data=f"increase-{item['book_id']}"),
                InlineKeyboardButton(item['title'], callback_data=f"default-{item['book_id']}"),
                InlineKeyboardButton("-", callback_data=f"decrease-{item['book_id']}"),
                InlineKeyboardButton("X", callback_data=f"clear-{item['book_id']}")
            ],
        )
        
    keyboards.append(
        [
            InlineKeyboardButton("Buyurtma berish", callback_data="complete-order"),
            InlineKeyboardButton("Savatni tozalash", callback_data="clear-cart")    
        ]
    )
    
    return InlineKeyboardMarkup(keyboards)

        
