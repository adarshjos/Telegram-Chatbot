import sys
import sqlite3
import time
import telepot
import  json 
import cStringIO

from PIL import Image
from pytesseract import image_to_string
from telepot.loop import MessageLoop
from urllib2 import urlopen


bot = telepot.Bot('429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0')
conne = sqlite3.connect('/root/eappan.db',check_same_thread=False)
# conn.execute("CREATE TABLE botocr(fileid varchar(1000),ocrdata varchar(2000))")
conn = conne.cursor()
def handle(msg):

	
		content_type, chat_type, chat_id = telepot.glance(msg)
		print(content_type, chat_type, chat_id)
		if content_type == 'photo' :

			print 'photo'
			length = (len(msg['photo'])-1)
			idfile=msg['photo'][length]['file_id']
			#bot.sendPhoto(chat_id,idfile)
			url = 'https://api.telegram.org/bot429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0/getFile?file_id='
			url=url+str(idfile)
			print url
			response = urlopen(url);
			data = json.loads(response.read())
			print(data)
			url1='https://api.telegram.org/file/bot429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0/'+data['result']['file_path']
			print(url1)
			file = cStringIO.StringIO(urlopen(url1).read())
			c=image_to_string(Image.open(file))
			l=c.split()
			#bot.sendMessage(chat_id, l)
			conn.execute("INSERT INTO botocr (fileid,ocrdata) VALUES (?,?)",((idfile),c));
			print("databse entered")
			conne.commit()
		elif content_type == 'text' :
			print msg
			print (msg['text'])
			find='%'+msg['text']+'%'
			print find
			conn.execute("SELECT fileid FROM botocr WHERE ocrdata LIKE ?",(find,));
			final=conn.fetchone()	
			print final[0]
			print type(final)	
			bot.sendPhoto(chat_id,final[0])
 



					
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
while 1:		
	time.sleep(10)																																															
