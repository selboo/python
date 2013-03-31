#coding=utf-8
import urllib2,os,re,sp_sql

buf = ""
temp_list = []
number = 0

def index(s, sub, start=0):
    for i in range(start,len(s)):
        p=i
        for j in sub:
            if j==s[p]: p+=1
            else: break
        else:
            return 1
    return 0

def dwon_url(url):
    global buf
    f = urllib2.urlopen(url, timeout=5)
    return f.read()
    
def parse(buf, url):
    global number
    s = re.findall("<a.*?href(.*?>).*?<\/a>", buf)
    for n in s:
        #temp_list.append(re.findall(r"""['" =]*(.*?)(?=['" >])""",n)[0])
        new_url = re.findall(r"""['" =]*(.*?)(?=['" >])""",n)[0]
        if index(new_url, "http") == 1:
            #print new_url.decode("gbk")
            nurl = new_url.decode("gbk")
            nurl = "".join(nurl.split())
            sp_sql.save_url(nurl)
            number = number + 1
    sp_sql.update_url(url)
    return "%s 获取URL %d 个" %(url, number)

while True:
    url = sp_sql.get_new_task()
    buf = dwon_url(url)
    print parse(buf, url)
    number = 0
    
#url = sp_sql.get_new_task()
#buf = dwon_url(url)
#parse(buf, url)

a = "javascrihttppt:void(0);"
#print index(a, 'http')