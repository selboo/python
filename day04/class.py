#coding:utf-8
class animal:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
#        print "self   id is ", id(self)
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,aaa):
        self.age = aaa
    def set_name(self,name):
        self.name = name
        
    def add_qq(self,qq111):
        self.qq = qq111
    def get_qq(self):
        return self.qq
        
m = animal("monkey", 23)
m.set_name("444")
m.set_age(11)

m.add_qq(123456)
print m.qq

name = m.get_name()
print name
age = m.get_age()
print age


monkey = animal("monk",10)
print "monkey id is ", id(monkey)
tiger = animal('TiG',5)
print "tiger  id is ", id(tiger)
print monkey.name
print monkey.age
print tiger.name
print tiger.age