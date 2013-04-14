#coding=utf-8

import urllib
import httplib2

http = httplib2.Http()
url="http://uliweb.clkg.org/login"
body={'username':'python','password':'python','rememberme':"True"}
headers={'Content-type':'application/x-www-form-urlencoded',
        "Connection": "Keep-Alive",
        "cache-control":"no-cache",
        }
response,content = http.request(url,'GET')

csrf_val = content.split('csrf_token" value="')[1].split('">')[0]
body['csrf_token'] = csrf_val
headers['Cookie']= response['set-cookie']

response,content = http.request(url,'POST',headers=headers,body=urllib.urlencode(body))
headers['Cookie']= response['set-cookie']

url='http://uliweb.clkg.org/forum'
response,content=http.request(url,'GET',headers=headers)


print content
print response
#c = http.request(url,'GET')
#print c[0][0]