__author__ = 'jhajduk'

import urllib2

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

u_sock = urllib2.urlopen(url)
data = u_sock.read()
u_sock.close()

# pull out the comment block at the end of the html

#here is our secret data
secret_data = data[data.rfind("<!--")+1:data.rfind("-->")]

counted = set([])

only1 = ""

for char in secret_data:
    if not char in counted:
        char_count = secret_data.count(char)
        counted.add(char)
        if char_count == 1:
            only1 = only1 + char

print only1