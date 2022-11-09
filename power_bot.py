import telebot
from telebot import types
from decouple import config


bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id, """<b><i>Hi, I am PowerBot, Calculate
     Commands for me
     
                    /start
                    
                    /current
                    
                    /count_power     
                                     </i></b>""", parse_mode='html')
     global k
     k = 'start'



@bot.message_handler(commands=['current'])
def start(message):
     bot.send_message(message.chat.id, '<b>Input Power of your Device </b>', parse_mode='html')
     global k
     k = 'current'
@bot.message_handler()
def get_user_text(message):
     d = 1
     #bot.send_message(message.chat.id, message.text, parse_mode='html')
     strings = message.text
     if k == 'current':
          try:

               d = int(strings) / 220
               bot.send_message(message.chat.id, f' Current of Device is : {round(d, 2)} A', parse_mode='html')
          except ValueError:
               bot.send_message(message.chat.id, f' Input correct power ', parse_mode='html')
     else:
          bot.send_message(message.chat.id, f' You are not choose a command ', parse_mode='html')


# @bot.message_handler(commands=['current'])
# def current(message):
#      bot.send_message(message.chat.id, f'Input Power of Device', parse_mode='html')
#      text = bot.message_handler()
#      print(text)
#      murkup = types.InlineKeyboardMarkup()
#      murkup.add(types.InlineKeyboardButton('calculation', callback_data="calc"))
#      bot.send_message(message.chat.id, f'Calculation', reply_markup=murkup)


bot.polling(none_stop=True)