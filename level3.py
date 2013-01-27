__author__ = 'jhajduk'

import urllib2

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

u_sock = urllib2.urlopen(url)
data = u_sock.read()
u_sock.close()

# pull out the comment block at the end of the html

# reverse string then find index of <!-- reversed
i1 = len(data) - data[::-1].index("--!<") + 1

# reverse string then find index of --> reversed
i2 = len(data) - data[::-1].index(">--") - 4

#here is our secret data
secret_data = data[i1:i2]

print secret_data

counted = set([])

only1 = ""

for char in secret_data:
    if not char in counted:
        char_count = secret_data.count(char)
        print "'"+char +"':"+str(char_count)
        counted.add(char)

        if char_count == 1:
            only1 = only1 + char

print only1