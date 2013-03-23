#coding=utf-8
import os,sys

file= open ("jeapedu.txt","w+r")
file.write("hello,")
file.write("a")
file.write("b")
l = file.read()
print l


print file.readline()
file.seek(3)
print file.tell()
file.close()

