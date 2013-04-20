#coding=utf-8

from uliweb.form import *

class blogform(Form):
    name    = StringField(label='姓名:', required=True)
    content = TextField(label='内容:')