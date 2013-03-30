#coding=utf-8

import urllib

def callback(down, block, size):
    #print down, block, size
    per = 100.0 * (down * block) / size
    if per > 100:
        per = 100
    print 'fdd %d' % (per),
    #print "asdf \r",
    
url = 'http://www.sina.com/'
local = 'sohu.html'
urllib.urlretrieve(url, local, callback)


