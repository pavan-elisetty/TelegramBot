import os
import telebot
import yfinance as yf


API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message,"hey! hows it going")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id,"hello") 



@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message,message.text+' This is the message that you sent')

bot.infinity_polling() # checks messages 