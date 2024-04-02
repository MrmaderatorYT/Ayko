import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Налаштування логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Створення датасету текстів та їх відповідей
text_dataset = {
    "привет": "Всем ку",
    "Как дела бот": "Та потихоньку. Жду следуйщею обнову моей версии",
    "спс": "Я не знаю что и ответить... Мне неловко....",
    "сиськи": "письки, а носки будут?"
    
}

# Функція, яка буде викликатися при команді /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Я бот, який відповідає на привітання.')

# Функція, яка буде викликатися при отриманні повідомлення
def reply_to_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()  # Перетворення тексту повідомлення в нижній регістр
    response = None
    
    for key_phrase, reply_text in text_dataset.items():
        if key_phrase in text:
            response = reply_text
            break
    
    if response:
        update.message.reply_text(response)
    #else:
     #   update.message.reply_text("Не розумію вашого повідомлення.")

def main() -> None:
    # Створення екземпляру Updater і передача токену бота
    updater = Updater("6136504891:AAHbIGEEUbPVLRGWm75QaaARujnx3vQ-Lpw")

    # Отримання диспетчера для реєстрації обробників
    dispatcher = updater.dispatcher

    # Реєстрація обробника команди /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Реєстрація обробника повідомлень
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message))

    # Запуск бота
    updater.start_polling()

    # Зупинка бота в разі отримання сигналу SIGINT (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()

