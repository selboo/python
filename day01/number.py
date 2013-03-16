#coding=utf-8

import random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)
f = random.randint(1,100)
g = random.randint(1,100)
h = random.randint(1,100)

print a,b,c,d,e,f,g,h

n = int(random.randint(1,100))
print n

min_m = 1
max_m = 100
y = 0
while True:
	while True:
		m = raw_input("请输入1-100数字:")
		if m.isalpha():
			print "请输入数字:"
			continue
		else:
			m = int(m)
			break

	if n == m:
		print "恭喜才对了 n = %d 您一共猜测了 %d" %(n,y)
		break
	elif n <= m:
		y = y + 1
		max_m = m
		print "您输入的数太大了 %d 范围在 %d-%d" %(m,min_m,max_m)
	elif n >= m:
		y = y + 1
		min_m = m
		print "您输入的数太小了 %d 范围在 %d-%d" %(m,min_m,max_m)



