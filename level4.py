__author__ = 'jhajduk'

import urllib2

url = "http://www.pythonchallenge.com/pc/def/equality.html"

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

#print secret_data

def match(str):
    if str[0].islower() and str[1].isupper() and str[2].isupper() and str[3].isupper() and str[4].islower() and str[5].isupper()  and str[6].isupper()  and str[7].isupper() and str[8].islower():
        return str[4]
    else:
        return ""

result = ""

for i in range(len(secret_data)-9):
    result += match(secret_data[i:i+9])

print result
