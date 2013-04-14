#coding=utf-8

import urllib
import httplib2

http = httplib2.Http()
url="http://192.168.2.202:8000"
body={'username':'Selboo','title':'title', 'content':'content'}
headers= {'Content-type':'application/x-www-form-urlencoded', 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:20.0) Gecko/20100101 Firefox/20.0'}
response,content=http.request(url,'POST',headers=headers,body=urllib.urlencode(body))

GET /ajax/accounthandler.ashx?t=log&u=u010278800&p=X0ce18d0Wi2i3S0cRNtsXsRDw50c850c8&remember=0&f=http%3A%2F%2Fwww.csdn.net%2F&enc=1&rand=0.6497961011469229 HTTP/1.1
Host: passport.csdn.net
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:20.0) Gecko/20100101 Firefox/20.0
Accept: */*
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest/ajax/accounthandler.ashx?t=log&u=u010278800&p=X0ce18d0Wi2i3S0cRNtsXsRDw50c850c8&remember=0&f=http%3A%2F%2Fwww.csdn.net%2F&enc=1&rand=0.6497961011469229
Referer: http://passport.csdn.net/account/loginbox?callback=logined&hidethird=1&from=http%3a%2f%2fwww.csdn.net%2f
Cookie: __utma=17226283.1578056252.1362305833.1364091496.1365824941.5; __utmz=17226283.1364091496.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=root%20%3D%20tk()%20nameerror%20name%20%27tk%27%20is%20not%20defined; __message_sys_msg_id=1849; __message_gu_msg_id=0; __message_cnel_msg_id=0; __utmb=17226283.14.10.1365824941; __utmc=17226283; CloudGuest=ETD96qeV7daGPj2GwADhWkULfd+WfHzIrjKCKsy1CngkhHRXgWkeTzRN0l9P0eyfY4WAuXQmT4tH30RGv470elnaD1kH1CO1qHof4u7zO0BNGdDv4/jYzYNnDP9HI5V3lQyyY4+IUveX1hRFbekMWmwULpYTCpUfC39/qk2szu5I4NC3eGZg7yGR4MgEPvut; sid=rnambqv53sed3ruipj0pxioh; __PongoUID=100; UN=u010278800; socketConnectstate=1365825317689; msgData=%26%261365825307911%26%260; __message_district_code=110000; __message_in_school=0
Connection: keep-alive



#print content
#c = http.request(url,'GET')
#print c[0][0]