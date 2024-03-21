import telebot
from telebot import types

bot = telebot.TeleBot('7098088538:AAH97YR51ZOBMdiu1CaHMmmtesqeSkpP2L8') 

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("❓ Помощь")
    btn2 = types.KeyboardButton("👀 Выбери порчу")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Привет! Я бот, наводящий порчу!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=="❓ Помощь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сколько по времени действует порча?')
        btn2 = types.KeyboardButton('Можно ли снять наложенную порчу?')
        btn3 = types.KeyboardButton('Советы по порчам')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,"Задайте интересующий вопрос", reply_markup=markup)

    elif message.text == 'Сколько по времени действует порча?':
        bot.send_message(message.from_user.id, 'В различных ситуациях по разному, некторые виды порчи работают до момента снятия', parse_mode='Markdown')
    elif message.text == 'Можно ли снять наложенную порчу?':
        bot.send_message(message.from_user.id, 'Можно, но только с помощью специалистов', parse_mode='Markdown')
    elif message.text == 'Советы по порчам':
        bot.send_message(message.from_user.id, 'Советы по порчам вы можете найти, пройдя по ' + '[ссылке](https://mirkrasim.ru/chjornaya-magiya/item/293-kak-sdelat-navesti-porchu-na-cheloveka)', parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=="👀 Выбери порчу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Порча на понос')
        btn2 = types.KeyboardButton('Порча на неудачу')
        btn3 = types.KeyboardButton('Порча на болезнь')
        btn4 = types.KeyboardButton('Порча на обидчика')
        btn5 = types.KeyboardButton('Порча на разлуку')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id,"Выбери порчу", reply_markup=markup)

    elif message.text == 'Порча на понос':
        bot.send_message(message.from_user.id, 'Вы навели порчу на понос', parse_mode='Markdown')
    elif message.text == 'Порча на неудачу':
        bot.send_message(message.from_user.id, 'Вы навели порчу на неудачу', parse_mode='Markdown')
    elif message.text == 'Порча на болезнь':
        bot.send_message(message.from_user.id, 'Вы навели порчу на болезнь', parse_mode='Markdown')
    elif message.text == 'Порча на обидчика':
        bot.send_message(message.from_user.id, 'Вы навели порчу на обидчика', parse_mode='Markdown')
    elif message.text == 'Порча на разлуку':
        bot.send_message(message.from_user.id, 'Вы навели порчу на разлуку', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)
