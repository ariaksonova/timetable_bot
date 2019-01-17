#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from time import sleep

my_dict = {u"Вторник": [], u"Среда": [], u"Четверг": [], u"Пятница": []}
url = "https://api.telegram.org/bot793609373:AAEBtNQw0CZo9rlW2gnAAXWMl-mFYUhcgL8/"
user_dict = dict()

def get_updates_json(request):
	#params = {'timeout': 50, 'offset': None}
	response  = requests.get(request + "getUpdates")#, data=params)
	return response.json()

def last_update(data):
	results = data['result']
	total_update = len(results) - 1
	return results[total_update]

def get_chat_id(update):
	chat_id = update['message']['chat']['id']
	return chat_id

def get_chat_text(update):
	chat_text = update['message']['text']
	return chat_text

def send_mess(chat, text):
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
		if update_id == last_update(get_updates_json(url))['update_id']:
			if get_chat_id(last_update(get_updates_json(url))) not in user_dict:
				user_dict[get_chat_id(last_update(get_updates_json(url)))] = list()
				send_mess(get_chat_id(last_update(get_updates_json(url))), 'Назви день недели (хочу от вторника до пятницы)')
			else:
				my_inf = user_dict[get_chat_id(last_update(get_updates_json(url)))]
				if len(my_inf) == 0 and get_chat_text(last_update(get_updates_json(url))) in my_dict:
					user_dict[get_chat_id(last_update(get_updates_json(url)))].append(get_chat_text(last_update(get_updates_json(url))))
					send_mess(get_chat_id(last_update(get_updates_json(url))), 'Чудно, напомни из какой ты групы? У нас их 3 если что!')
				elif len(my_inf) == 0:
					send_mess(get_chat_id(last_update(get_updates_json(url))), "Сорян, Маша написала меня на коленке, поэтому я тупенький и мы говорил на разных языках(\nМожет попробуешь написать с большой буквы?")
					user_dict.pop(get_chat_id(last_update(get_updates_json(url))))
				elif len(my_inf) == 1:
					val = get_chat_text(last_update(get_updates_json(url)))
					if RepresentsInt(val) and int(val) >= 1 and int(val) <= 3:
						user_dict[get_chat_id(last_update(get_updates_json(url)))].append(int(get_chat_text(last_update(get_updates_json(url)))))
						user_dict.pop(get_chat_id(last_update(get_updates_json(url))))
					else:
						send_mess(get_chat_id(last_update(get_updates_json(url))), 'Ха-ха-ха, ты такой смешной. Нет. Попробуй еще раз)')
						user_dict.pop(get_chat_id(last_update(get_updates_json(url))))
			update_id += 1
		sleep(1)       

if __name__ == '__main__':  
    main()



# day = get_chat_text(last_update(get_updates_json(url)))
			# if day in my_dict.keys():
			# 	send_mess(get_chat_id(last_update(get_updates_json(url))), 'Чудно, напомни из какой ты групы? У нас их 3 если что!')
			# 	group = get_chat_text(last_update(get_updates_json(url)))
			# 	if group > 3 or group < 1:
			# 		send_mess(get_chat_id(last_update(get_updates_json(url))), 'Ха-ха-ха, ты такой смешной. Нет.')
			# else:
			# 	send_mess(get_chat_id(last_update(get_updates_json(url))), 'Сорян, Маша написала меня на коленке, поэтому я тупенький и мы говорил на разных языках(')
			# send_mess(get_chat_id(last_update(get_updates_json(url))), 'Назви день недели (хочу от вторника до пятницы)')
			