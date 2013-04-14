#coding=utf-8

import urllib
import httplib2

http = httplib2.Http()

#u010278800
#1234567890
url = "http://passport.csdn.net/ajax/accounthandler.ashx?t=log&u=u010278800&p=X0ce18d0Wi2i3S0cRNtsXsRDw50c850c8&remember=0&f=http%3A%2F%2Fwww.csdn.net%2F&enc=1&rand=0.6497961011469229"

url_get = "http://passport.csdn.net/account/login"
response,content = http.request(url_get,'GET')
#print response
#print content

body={'u':'u010278800','p':'X0ce18d0Wi2i3S0cRNtsXsRDw50c850c8', 'rand':'0.6497961011469229'}
headers= {'Content-type':'application/x-www-form-urlencoded', 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:20.0) Gecko/20100101 Firefox/20.0', 'data':'123123'}
response,content=http.request(url,'POST',headers=headers,body=urllib.urlencode(body))
print response
print content

#print content
#c = http.request(url,'GET')
#print c[0][0]
