#coding=utf-8

import urllib
import httplib2

http = httplib2.Http()
url="http://uliweb.clkg.org/login"
#response,content=http.request(url,'GET')
#print content
c = http.request(url,'GET')
print c[0][0]