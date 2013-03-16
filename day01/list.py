import os,sys

a = [1,"222","a",4,5,6,"e",8,"c"]
n = a
b = []

for i in range(0,len(a)):
    b.append(a.pop())

print n
print b