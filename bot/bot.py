import telebot
from listas import *

TOKEN = "514563961:AAH4G5EC0Cta6KNvvGQZpx2QJGCL2e-2uFA"
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Comandos disponibles:\n\n/lists: muestra las listas existentes\n/list: muestra una lista en concreto a partir de un nombre dado\n/addlist: crea una nueva lista a partir de un nombre dado\n/addfilm: añade una película (proporcionando nombre y opcionalemente una puntuación) a una lista dada\n/removelist: elimina una lista")

@bot.message_handler(commands=['lists'])
def send_lists(message):
	lists = getLists()

	resp = ""

	for k,v in lists.items():
	    resp += k
	    resp += '\n\n'
	    for k2,v2 in v[0].items():
	        resp += k2
	        resp += ' '
	        resp += str(v2)
	        resp += '\n'
	    resp += '____________\n\n'

	bot.reply_to(message, resp)

bot.polling()