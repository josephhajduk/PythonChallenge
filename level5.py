__author__ = 'jhajduk'

import urllib2

links = set([])
linkmap = {}

def get_url(url):
    u_sock = urllib2.urlopen(url)
    data = u_sock.read()
    u_sock.close()
    return data

def next_nothing(url):
    result = get_url(url)
    print result
    return result[result.find("next nothing is ")+16:]

first_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

url_prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

depth = 0

def go_dj(nothing):
    global depth

    depth += 1

    print depth

    if nothing in links:
        go_dj(linkmap[nothing])
    else:
        n_nothing = next_nothing(url_prefix+nothing)
        links.add(nothing)
        linkmap[nothing] = n_nothing
        go_dj(n_nothing)

print next_nothing(url_prefix+"66831")
#82930