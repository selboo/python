#coding=utf-8

import urllib
import httplib2

http = httplib2.Http()
url="http://uliweb.clkg.org/login"

response,content = http.request(url,'GET')
share_token = content.split('csrf_token" value="')[1].split('">')[0]
share_cookie = response['set-cookie']

body={'username':'python','password':'python','rememberme':"True"}
headers={'Content-type':'application/x-www-form-urlencoded',
        "Connection": "Keep-Alive",
        "cache-control":"no-cache",
        "csrf_token" : share_token,
        "Cookie" : share_cookie,
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:20.0) Gecko/20100101 Firefox/20.0'
        }

#登陆
response,content = http.request(url,'POST',headers=headers,body=urllib.urlencode(body))
print headers['Cookie']
print response['set-cookie']
#print response
#print content

url='http://uliweb.clkg.org/forum'
response,content=http.request(url,'GET',headers=headers)
#print response
#print content
#c = http.request(url,'GET')
#print c[0][0]