#coding:utf-8

import requests, base64, re, hashlib
sha1 = lambda x : hashlib.sha1(x).hexdigest()

webclient = 'ssplogin.js(v.1.3.18)'

username = 'selboogo@126.com'

session = requests.Session()

resp = session.get(
'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sina'
'SSOController.preloginCallBack&su=%s&client=%s' %
(base64.b64encode(username), webclient)
)
content = resp.content
servertime = re.findall('"servertime":(\d*)', content)
nonce      = re.findall('"nonce":"(.*)",', content)
#nonce      = content.split('nonce":"')[1].split('"')[0]
print servertime
print nonce
print content