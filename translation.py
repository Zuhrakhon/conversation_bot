TRANSLATION = {
    "salom": {
        "uz": "Salom", 
        "ru": "Привет",
        "en": "Hello"
    }, 
    "bot salom": {
        "uz": "Assalomu alaykum\nBotimizga xush kelibsiz",
        "ru": "Приветствуем вас нашим ботом",
        "en": "Hello, welcome to our bot"
    },
    "change language": {
        "uz": "UZ Til o'zgartirildi",
        "ru": "RU Til o'zgartirildi",
        "en": "EN Til o'zgartirildi"
    },
    "books": {
        "uz": "📕 Kitoblar",
        "ru": "📕 Книги",
        "en": "📕 Books"
    }
}

def get_translation(word, language):
    if not language:
        language = "uz"
        
    text = TRANSLATION.get(word, {}).get(language)
    return text if text else word