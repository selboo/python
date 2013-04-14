# -*- coding: utf-8 -*-

import urllib2, urllib, cookielib
import re, json, base64
import rsa, binascii


url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.5)&_=1364875106625'
url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)'

class Toy(object):
    def fecth_page(self, url = 'http://weibo.com', data = None):
        return self.__opener.open(url, data)
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:19.0) Gecko/20100101 Firefox/19.0')]
        self.__opener = opener
        
        self.__login()
        
    def __encode_passwd(self, pwd, servertime, nonce, pubkey):
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(pwd)#拼接明文 js加密文件中得到
        passwd = rsa.encrypt(message, key)#加密
        passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
        return passwd

    def __encode_username(self, username):
        username = urllib.quote(username)
        username = base64.encodestring(username)[:-1]
        return username
    
    def __prelogin(self):
        html = self.__opener.open(url_prelogin).read()
        json_data = re.search('\((.*)\)', html).group(1)
        data = json.loads(json_data)
        servertime = data['servertime']
        nonce = data['nonce']
        pubkey = data['pubkey']
        rsakv = data['rsakv']
        return servertime, nonce, pubkey, rsakv
    
    def __login(self):
        (servertime, nonce, pubkey, rsakv) = self.__prelogin()
        sp = self.__encode_passwd(self.__password, servertime, nonce, pubkey)
        su = self.__encode_username(self.__username)
        postdata = {
                    'entry': 'weibo',
                    'gateway': '1',
                    'from': '',
                    'savestate': '7',
                    'userticket': '1',
                    'ssosimplelogin': '1',
                    'vsnf': '1',
                    'vsnval': '',
                    'su': su,
                    'service': 'miniblog',
                    'servertime': servertime,
                    'nonce': nonce,
                    'pwencode': 'rsa2',
                    'sp': sp,
                    'encoding': 'UTF-8',
                    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                    'returntype': 'META',
                    'rsakv' : rsakv,
                    }


        postdata = urllib.urlencode(postdata)
        html = self.__opener.open(url_login, postdata).read()
        print html
        url_final = re.search('location\.replace\(\"(.*?)\"\)', html).group(1)
        self.__opener.open(url_final)

        print url_final
