import sys
import sqlite3
import time
import telepot
from telepot.loop import MessageLoop
import  json
from urllib2 import urlopen
url = 'https://api.telegram.org/bot429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0/getFile?file_id='


conn = sqlite3.connect('eappan.db')
bot = telepot.Bot('429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0')
def handle(msg):
	
		content_type, chat_type, chat_id = telepot.glance(msg)
		print(content_type, chat_type, chat_id)
		if content_type == 'text':
			if msg['text'] in ['hello','hi']:
		 
				bot.sendMessage(chat_id, msg['text'])
					
			else:
				bot.sendMessage(chat_id, "Start With Hi or Hello to talk with me!!")
		else:
				if content_type == 'document':
					# bot.sendDocument(chat_id,msg['document']['file_id'])
					# print (msg['document']['file_size'])
					# print (msg['document']['file_id'])
					idfile=msg['document']['file_id']
					url = 'https://api.telegram.org/bot429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0/getFile?file_id='
					url=url+str(idfile)
					print url
					response = urlopen(url);
					data = json.loads(response.read())
					print(data)
					url1='https://api.telegram.org/file/bot429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0/'+data['result']['file_path']
					print(url1)

					



					
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
while 1:		
	time.sleep(10)																																															