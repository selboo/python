#coding=utf-8
import os,sys

a = {}
a["name"] = "Tom"
a["age"] = "20"
a["qq"] = "123456"
a["email"] = "qq@qq.com"

a["name"] = "Peter"
a["age"] = "30"
a["qq"] = "654321"
a["email"] = "123456@qq.com"

b = {'qq': '111111', 'age': '90', 'name': 'Tom', 'email': 'qq@qq.com'},{'qq': '654321', 'age': '30', 'name': 'Peter', 'email': '123456@qq.com'}
print b
#print type(b[0].items())

for n in range(0,len(b)):
    print "=========== 分段符 ==========="
    for k,v in b[n].items():
        print "%s::::%s" %(k,v)


print b[0].get("name")





