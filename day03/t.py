#coding=utf8

#start = raw_input("起点：")
#stop  = raw_input("起点：")
start = "文慧桥"
stop = "知春路"

f = open("bus.txt")
dict_list = f.readlines()
f.close()

for n in range(0, len(dict_list)):
    
    bus_list = dict_list[n].split(":")[1]
    print bus_list
    bus_list_len = len(bus_list.split(","))
    
    bus_list = dict_list[n].split(":")[1]
    bus_list_len = len(bus_list.split(",")