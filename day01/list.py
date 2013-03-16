import os,sys

a = [1,"222","a",4,5,6,"e",8,"c"]
n = a[:]
b = []

for i in range(0,len(a)):
    b.append(a.pop())

print n
print b
print "========================="
a1 = "\t\t\hello\n.py\n\n\n"
a2 = r"\t\t\hello\n.py\n\n\n"
a3 = "\hello\n.py"
a4 = r"\hello\n.py"

print a1
print a2
print a3
print a4
print "========================="
print a1.strip()
print a2.strip()
print a3.strip()
print a4.strip()



