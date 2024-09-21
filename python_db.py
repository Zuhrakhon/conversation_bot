BOOKS = [
    {
        "id": 1,
        "title": "Sariq devni minib",
        "price": 25000,
        "description": """Dev ulkan, baland bo'yli va kuchli, terisi esa yorqin sariq rangda nur sochib turadi. 
        Devning yirik, dag'al qo'llari yerni titratadigan qadamlar bilan yurib boradi. 
        Uning yuzi qahrli va ko'zlari chaqnab turadi. """,
        "_type": "paper",
        "cover": "https://avatars.mds.yandex.net/i?id=5646757dbb75bf6cbce3b3b94371a0d2-4893181-images-thumbs&n=13"
    },
    {
        "id": 2,
        "title": "Dastur tashkiloti",
        "price": 15000,
        "description": """Dastur tashkiloti, yoki dastur qo'shish tashkiloti, yoki dastur qo'shish qizil uchun qo'shish tashkiloti,
        juda yaxshi bo'lishi kerak. Dastur tashkiloti o'zining qizil uchun qo'shish tashkiloti qilishga yordam beradi.""",
        "_type": "paper",
        "cover": "https://avatars.mds.yandex.net/i?id=5646757dbb75bf6cbce3b3b94371a0d2-4893181-images-thumbs&n=13"
    },
    {
        "id": 3,
        "title": "G'ayriixtiyoriy ong mo'jizalari",
        "price": 30000,
        "description": """Qizil uchun qo'shish tashkiloti, yoki qizil uchun qo'shish tashkiloti, yoki qizil uchun qo'shish tashkiloti,
        juda yaxshi bo'lishi kerak. Qizil uchun qo'shish tashkiloti o'zining qizil uchun qo'shish tashkiloti qilishga yordam beradi.""",
        "_type": "audio",
        "cover": "https://avatars.mds.yandex.net/i?id=5646757dbb75bf6cbce3b3b94371a0d2-4893181-images-thumbs&n=13"
    },
    {
        "id": 4,
        "title": "Ertaklar",
        "price": 56300,
        "description": """Sariq qizil uchun qo'shish tashkiloti, yoki sariq qizil uchun qo'shish tashkiloti, yoki sariq qizil uchun qo'shish tashkiloti,
        juda yaxshi bo'lishi kerak. Sariq qizil uchun qo'shish tashkiloti o'zining qizil uchun qo'shish tashkiloti qilishga yordam beradi.""",
        "_type": "paper",
        "cover": "https://avatars.mds.yandex.net/i?id=5646757dbb75bf6cbce3b3b94371a0d2-4893181-images-thumbs&n=13"
        
    },
    {
        "id": 5,
        "title": "Kompozitor",
        "price": 12777,
        "description": """Kompozitor, yoki kompozitor, yoki kompozitor, yoki kompozitor, yoki kompozitor,
        juda yaxshi bo'lishi kerak. Kompozitor o'zining qizil uchun qo'shish tashkiloti qilishga yordam beradi.""",
        "_type": "audio",
        "cover": "https://avatars.mds.yandex.net/i?id=5646757dbb75bf6cbce3b3b94371a0d2-4893181-images-thumbs&n=13"
    }
]


def get_book_id(book_id: int) -> dict:
    for book in BOOKS:
        if book['id'] == book_id:
            return book
    
    return None