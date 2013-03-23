#coding=utf-8

f = open("dict.txt")
dict_list = f.readlines()
f.close()

dict_data = {}

for n in dict_list:
    n_list = n.split(":")
    dict_data[n_list[0]] = n_list[1]
    
word = raw_input("Please input a word:")

print dict_data[word]