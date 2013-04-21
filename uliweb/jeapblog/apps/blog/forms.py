#coding=utf-8

from uliweb.form import *

class blogform(Form):
    #name    = StringField(label='姓名:', required=True)
    title   = StringField(label='主题')
    content = TextField(label='内容')
    

class blogform_content(Form):
    content = TextField(label='内容')