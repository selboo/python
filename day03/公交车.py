#coding=utf8

#start = raw_input("起点：")
#stop  = raw_input("起点：")
start = "aaa"
stop  = "777"
print start
print stop
f = open("bus.txt")
dict_list = f.readlines()
f.close()

for n in range(0, len(dict_list)):
    bus_list = dict_list[n].split(":")[1].strip('\n')
    if start in bus_list:
        start_bus_list = bus_list.split(",")[:]
        bus_num_start = dict_list[n].split(":")[0].strip('\n')
        if stop in bus_list:
            car_list = bus_list.split(",")
            s = car_list.index(start)
            t = car_list.index(stop)
            m = s + t
            a = "直通车"
            print "%s %s" %(a, car_list[s:m])
            exit()

for n in range(0, len(dict_list)):
    bus_list = dict_list[n].split(":")[1].strip('\n')
    if stop in bus_list:
        bus_mun_stop = dict_list[n].split(":")[0].strip('\n')
        stop_bus_list = bus_list.split(",")[:]
        
print start_bus_list
print stop_bus_list

b3 = list(set(start_bus_list) & set(stop_bus_list))

for l in range(0, len(start_bus_list)):
    if start_bus_list[l] == ''.join(b3):
        start_bus_list_num_s = l
    if start_bus_list[l] == start:
        start_bus_list_num_t = l
        
for l in range(0, len(stop_bus_list)):
    if stop_bus_list[l] == ''.join(b3):
        stop_bus_list_num_s = l
    if stop_bus_list[l] == stop:
        stop_bus_list_num_t = l

if start_bus_list_num_s > start_bus_list_num_t:
    s0 = start_bus_list_num_t
    s1 = start_bus_list_num_s
    start_bus_list_num_s = s0
    start_bus_list_num_t = s1
    
if stop_bus_list_num_s > stop_bus_list_num_t:
    s0 = stop_bus_list_num_t
    s1 = stop_bus_list_num_s
    stop_bus_list_num_s = s0
    stop_bus_list_num_t = s1
    
start_bus_list_list = start_bus_list[start_bus_list_num_s:start_bus_list_num_t+1]
stop_bus_list_list =  stop_bus_list[stop_bus_list_num_s:stop_bus_list_num_t+1]

print "公交站 %s 站 --> %s 站 一下到车路径" %(start,stop)
print "在%s路公交车 乘坐 %s 到 %s 路 到终点 %s" %(bus_num_start,start_bus_list_list,bus_mun_stop,stop_bus_list_list)
#print start_bus_list[]
#print start_bus_list[2]
#print ''.join(b3)

#l1 = ['aaa']
#l2 = "aaa"
#
#print type(b3)
#print ''.join(b3)
#start_bus_list.index(b3)

#    if stop in bus_list:
#        stop_bus_list = bus_list
    #print start_bus_list
    #b3=list(set(start_bus_list) & set(stop_bus_list))
    #print b3
    
#    bus_list_len = len(bus_list.split(","))
#    for i in range(0,bus_list_len):
#        #print bus_list
#        pass
    #print dict_list[n]
    #zhanhao_zhanming = dict_list[n].split(":")
    #print zhanhao_zhanming
    #zhanming_list = zhanhao_zhanming[1].split(",")
    #if start in zhanming_list:
    #    print zhanming_list.index(start)
#    for n in range(0, len(zhanming_list)):
#        if start in zhanming_list[0]:
#            print "111"
#            if stop in zhanming_list[0]:
#                print "222"
#            if start in zhanming_list[n]:
#                print "112"
        #if zhanming_list[n] == start:
        #    if stop in zhanhao_zhanming[n]:
        #        print 11
            #print zhanhao_zhanming[0]
            #print start
            #print zhanming_list.index(start)
    #print zhanming_list.find(start)
    

#f = open("bus.txt")
#for line in f:
#    pass
#    print line
#    print line.split(":")
#    zhanhao = line.split(":")
#    chehao = int(zhanhao[0])
#    
#    print chehao
#    zhanpai_num = 0
#    for n in zhanhao[1].split(","):
#        zhanpai_num += 1
#        print "%d  %s  %d" %(chehao, n.strip('\n'), zhanpai_num)
        
        
#    zhanming = zhanhao[1].split(",")
#    print zhanming[0]
#    
#    zhanhao[0] = {}
#    print zhanhao[0]
