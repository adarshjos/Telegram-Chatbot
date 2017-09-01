from PIL import Image
from pytesseract import image_to_string
import urllib, cStringIO
file = cStringIO.StringIO(urllib.urlopen('https://api.telegram.org/file/bot429545323:AAEj3Pqo3ItuNWGefbJjy4N-lwrqzOseZD0/documents/file_26.jpg').read())
c=image_to_string(Image.open(file))
l=c.split()


print c
print "\n\n\n"
print l
