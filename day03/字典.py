#coding=utf-8

input_str = raw_input("请输要查找的字典")

local_dict = {}

f = open("dict.txt")
for line in f:
    n_str = line.split(":")
    local_dict[n_str[0]] = n_str[1]
    if n_str[0] == input_str:
        print "%s 的意思是 %s" %(n_str[0],n_str[1])
f.close()