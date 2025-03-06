from telebot import TeleBot, types

# Вставьте сюда ваш токен от бота
API_TOKEN = '8112890542:AAFlt2iux2b1_0B4QX-EmxJqE47itld41GI'

# Создаем объект бота
bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message, "И тебе всего хорошего!!!")

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки сообщений
    bot.polling()
