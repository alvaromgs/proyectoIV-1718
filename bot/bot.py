import telebot
from listas import *

TOKEN = "514563961:AAH4G5EC0Cta6KNvvGQZpx2QJGCL2e-2uFA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Comandos disponibles:\n\n/lists: muestra las listas existentes\n/list: muestra una lista en concreto a partir de un nombre dado\n/addlist: crea una nueva lista a partir de un nombre dado\n/film: añade o actualiza una película proporcionando la lista a la que se va a añadir o en la que ya existe, el nombre de la película y opcionalmente una puntuación (si no se especifica será 0)\n/removelist: elimina una lista a partir de un nombre dado\n\nEn el caso de utilizar un comando que requiera parámetros, estos irán separados por asteriscos. Ejemplos:\n\n/addlist Pendientes\n/addfilm Favoritas*Origen*9")

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

@bot.message_handler(commands=['list'])
def send_list(message):
	m = message.text
	m = m[6:]
	l = getList(m)
	if l:
		resp = ''
		resp += m
		resp += '\n\n'
		for k, v in l[0].items():
			resp += k
			resp += ' '
			resp += str(v)
			resp += '\n'
		bot.reply_to(message,resp)
	else:
		bot.reply_to(message,'No existe una lista con ese nombre')

@bot.message_handler(commands=['addlist'])
def send_list(message):
	m = message.text
	m = m[9:]
	if '*' not in m:
		addList(m)
		bot.reply_to(message,'Lista creada correctamente')
	else:
		bot.reply_to(message,"El nombre de una lista no puede contener el carácter '*'")

@bot.message_handler(commands=['film'])
def send_list(message):
	m = message.text
	m = m[6:]
	if '*' not in m:
		command_error(message)
	else:
		param = m.split('*')
		if len(param) < 2:
			bot.reply_to(message,"Debes proporcionar al menos el nombre de la lista a la que vas a añadir la película y el título de la misma")
		else:
			nota = 0
			if len(param) == 3:
				nota = param[2]
			res = updateMovie(param[0],param[1],nota)
			if not res:
				bot.reply_to(message,"No existe una lista con ese nombre")
			else:
				bot.reply_to(message,"Película añadida correctamente")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_error(message):
	bot.reply_to(message, 'Comando incorrecto. Puedes consultar la ayuda del bot con /help')

bot.polling(none_stop=True)