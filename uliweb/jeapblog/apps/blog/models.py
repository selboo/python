#coding=utf-8
from uliweb.orm import *
import datetime


class blogm(Model):
    name     = Field(CHAR)
    title    = Field(TEXT)
    content  = Field(TEXT)
    datetime = Field(datetime.datetime, auto_now_add=True)