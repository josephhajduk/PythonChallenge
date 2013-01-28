__author__ = 'jhajduk'

import urllib2

url = "http://www.pythonchallenge.com/pc/def/equality.html"

u_sock = urllib2.urlopen(url)
data = u_sock.read()
u_sock.close()

# pull out the comment block at the end of the html

secret_data = data[data.rfind("<!--")+1:data.rfind("-->")]

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
