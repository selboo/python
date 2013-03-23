#coding=utf-8
import os,sys

number = raw_input("请输入数字:")
Symbol = filter(lambda ch: ch in '+|-|*|/', number)
set = number.split(Symbol)

if number.find('+') > 0:
    ret_str = number.split('+')
    print int(ret_str[0]) + int(ret_str[1])
if number.find('-') > 0:
    ret_str = number.split('-')
    print int(ret_str[0]) - int(ret_str[1])
if number.find('*') > 0:
    ret_str = number.split('*')
    print int(ret_str[0]) * int(ret_str[1])
if number.find('/') > 0:
    ret_str = number.split('/')
    print int(ret_str[0]) / int(ret_str[1])


number0 = int(set[0])
number1 = int(set[1])

if Symbol == '+':
    Result = number0 + number1
elif Symbol == '-':
    Result = number0 - number1
elif Symbol == '*':
    Result = number0 * number1
elif Symbol == '/':
    Result = number0 / number1
    
print "%d %s %d = %d" %(number0,Symbol,number1,Result)
