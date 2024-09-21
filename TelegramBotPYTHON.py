
# Подключаем модуль для Телеграма
import telebot
import telebot.types
from telebot import types
import os
# Указываем токен
bot = telebot.TeleBot('YouTelegramBotToken')



@bot.message_handler(content_types=['text'])
def start(message):
    """
    Fubction start of message


    .. note::

        .. recomends::
        -You can use this function on your code. Text in list of if you can edit\n-It is advisable not to use the function like this 'start(...)' 
        


    """
    userid = message.from_user.id
    username = message.from_user.first_name

    markup = types.InlineKeyboardMarkup()

    lockedcommands = ['/start', '/commands', 'description', 'reg_chat', '/serverip', '/link']
    

    if message.text == '/start':
        bot.send_message(message.from_user.id, f"Привет {username}!\nДля вывода комманд введи /commands")
    elif message.text == '/commands':
        bot.send_message(message.from_user.id, "Доступные комманды:\n/info - получение информации о боте и вашем id\n/description - для чего нужен бот\n/serverip - получение ip сервера MONDESTCRAFT\n/link - привязка аккаунта аккаунта сервера в майнкравт к телеграмм боту")
    elif message.text == '/info':
        bot.send_message(message.from_user.id, f"Ваш id пользователя телеграмм {userid}")
    elif message.text == '/description':
        markup.add(types.InlineKeyboardButton('Перейти в телеграм канал', url= 'https://t.me/+HQMazdrRixVlZTEy'))
        bot.send_message(message.from_user.id, "Бот создан для того чтобы вы могли связать свой аккаунт в боте и наш сервер в майнкрафт", parse_mode='html', reply_markup=markup)
    elif message.text == '/reg_chat':
        bot.send_message(message.chat.id, "В следующем сообщении напишите имя для chat accaunt")
        if message.text == lockedcommands:
            bot.send_message(message.chat.id, "Напиши имя эти комманды заблокированны")
            if message.text != lockedcommands:
                with open("database.txt"):
                    f = open("database.txt", 'w+')
                    f.write(f"{message}")
            else:
                bot.send_message(message.chat.id, "Напиши имя эти комманды заблокированны")
        else:
            bot.send_message(message.chat.id, "Напиши имя эти комманды заблокированны")
    elif message.text == '/serverip':
        bot.send_message(message.from_user.id, "Ip сервера находится в разработке")
    elif message.text == '/link':
        bot.send_message(message.from_user.id, "Подскажи где взять ТАКОЙ ПЛАГИН😈")
    else:
        bot.send_message(message.from_user.id, "Это не известная для меня комманда\nДля показа доступных комманд введи /commands")

bot.set_my_commands(
   commands=[
      telebot.types.BotCommand('info', 'Получение вашего айди'),
      telebot.types.BotCommand('serverip', 'получение ip сервера MONDESTCRAFT'),
      telebot.types.BotCommand('description', 'для чего нужен бот'),
      telebot.types.BotCommand('reg_chat', 'регестрация чата в бот cloud')
    ]
)



bot.polling(none_stop=True, interval=0)

