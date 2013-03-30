#coding=utf-8
import urllib2,os

def leng(aurl):
    handler = urllib2.HTTPHandler()
    request = urllib2.Request(url=aurl)
    f = urllib2.urlopen(request)
    return f.headers['content-length']

def get_mp3(aurl, start_leng, stop_leng, mp3file):
    handler = urllib2.HTTPHandler()
    request = urllib2.Request(url=aurl)
    request.headers['Range'] = 'bytes=%s-%s' % (start_leng, stop_leng)
    f = urllib2.urlopen(request)
    r = write_file(f.read(), mp3file)
    if r == 0:
        print "%s 文件 %d - %d段 完成\r" % (mp3file, start_leng, stop_leng),;

def write_file(binary, mp3file):
    file = open (mp3file, "a")
    file.write(binary);
    file.close()
    return 0

def down_list(aurl, number, mp3file):
    mp3_leng = int(leng(aurl))
    global start,stop
    g = mp3_leng / number
    start = 0
    stop = g
    for i in range(0,number):
        if stop < mp3_leng:
            get_mp3(aurl, start, stop, mp3file)
            start = stop + 1
            stop = stop + g

    if stop <= mp3_leng:
        get_mp3(aurl, start, mp3_leng, mp3file)
        
    return 0

aurl = 'http://zhangmenshiting.baidu.com/data2/music/35582819/355670791364623261128.mp3?xcode=27b5ecc2e69307c8aee64b0fbfb4525a'
mp3name = "a.mp3"
#print int(leng(aurl))
r = down_list(aurl, 10, mp3name)
if r == 0:
    print "下载完成,开始播放 %s" % mp3name
    #os.system('/usr/bin/rhythmbox a.mp3')




