#coding=utf-8
import urllib2,os

global url_number
url_number = 0
aurl = "<a href='http://ting.sohu.com/' target=_blank>国学与领导力</a><a href='http://www.baidu.com' target=_blank>国学与领导力</a><a href='http://www.google.com' target=_blank>国学与领导力</a>"


def index(s, sub, start=0):
    num = 0
    for i in range(start,len(s)):
        p=i
        for j in sub:
            if j==s[p]: p+=1
            else: break
        else:
            idx=i
            num = num + 1
    return num

def get_url(url):
    #print url
    #aurl_low = url.lower()
    aurl_low = url
    aurl_href_Number = index(aurl_low, 'href=')
    #print aurl_href_Number
    if aurl_href_Number != 0:
        for i in range(0, aurl_href_Number):
            #print i
            aurl_Left_Number = aurl_low.find('href=')
        
        
            aurl_Left = aurl_low[aurl_Left_Number+6:]
        
            aurl_Right_Number = aurl_Left.find('"')
            if aurl_Right_Number < 0 :
                aurl_Right_Number = aurl_Left.find("'")
            aurl_Right = aurl_Left[:aurl_Right_Number]
        
            #print aurl_Right
            
            aurl_low = aurl_low[aurl_low.find(aurl_Right)+len(aurl_Right):]
            print aurl_low
            #url_number += 1
    
    
f = urllib2.urlopen('http://www.hao123.com/')
a = f.read()

file_url = open("a.txt", "w")
file_url.write(a);
file_url.close()


file_read = open("a.txt")

while 1:
    line = file_read.readlines()
    if not line:
        break
    get_url(line)
    #print line
print url_number