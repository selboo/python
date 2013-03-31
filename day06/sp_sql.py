#coding=utf-8
from uliweb.orm import *

db=get_connection('mysql://root:123456@localhost/spider?charset=utf8')

class spider_url(Model):
    url    = Field(str)
    status = Field(str)

def save_url(url):
    n = spider_url.get(spider_url.c.url == url)
    if n:
        return
    n = spider_url()
    n.url = url
    n.status = "0"
    n.save()
    
def update_url(url):
    n = spider_url.get(spider_url.c.url == url)
    n.status = "1"
    n.save()
    
def get_new_task():
    n = spider_url.get(spider_url.c.status == "0")
    return n.url
   
def get_url(id):
    n = spider_url.get(spider_url.c.id == id)
    return n.url

#db.metadata.create_all()
#save_url("http://www.sina.com.cn/")
#save_url("http://www.sohu.com/")
#save_url("http://www.qq.com/")
#save_url("http://www.163.com/")
#update_url("http://www.baidu.com/")
print get_url('96')

