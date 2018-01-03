import telebot
from listas import *

TOKEN = "514563961:AAH4G5EC0Cta6KNvvGQZpx2QJGCL2e-2uFA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Comandos disponibles:\n\n/lists: muestra las listas existentes\n/list: muestra una lista en concreto a partir de un nombre dado\n/addlist: crea una nueva lista a partir de un nombre dado\n/film: añade o actualiza una película proporcionando la lista a la que se va a añadir o en la que ya existe, el nombre de la película y opcionalmente una puntuación (si no se especifica será 0)\n/rmlist: elimina una lista a partir de un nombre dado\n/rmfilm: elimina una película proporcionando la lista en la que se encuentra y el título de la misma\n\nEn el caso de utilizar un comando que requiera parámetros, estos irán separados por asteriscos. Ejemplos:\n\n/addlist Pendientes\n/addfilm Favoritas*Origen*9")

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
def add_list(message):
	m = message.text
	m = m[9:]
	if '*' not in m:
		addList(m)
		bot.reply_to(message,'Lista creada correctamente')
	else:
		bot.reply_to(message,"El nombre de una lista no puede contener el carácter '*'")

@bot.message_handler(commands=['film'])
def add_film(message):
	m = message.text
	m = m[6:]
	if '*' not in m:
		command_error(message)
	else:
		param = m.split('*')
		nota = 0
		if len(param) == 3:
			nota = param[2]
		res = updateMovie(param[0],param[1],nota)
		if not res:
			bot.reply_to(message,"No existe una lista con ese nombre")
		else:
			bot.reply_to(message,"Película añadida correctamente")

@bot.message_handler(commands=['rmlist'])
def remove_list(message):
	m = message.text
	m = m[8:]
	l = removeList(m)
	if l:
		bot.reply_to(message,'Lista borrada correctamente')
	else:
		bot.reply_to(message,'No existe una lista con ese nombre')

@bot.message_handler(commands=['rmfilm'])
def remove_film(message):
	m = message.text
	m = m[8:]
	if '*' not in m:
		command_error(message)
	else:
		param = m.split('*')
		res = removeMovie(param[0],param[1])
		if not res:
			bot.reply_to(message,"No existe una película con ese nombre en la lista proporcionada")
		else:
			bot.reply_to(message,"Película borrada correctamente")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_error(message):
	bot.reply_to(message, 'Comando incorrecto. Puedes consultar la ayuda del bot con /help')

bot.polling(none_stop=True)