
class Toy(object):
    def fecth_page(self, url = 'http://weibo.com', data = None):
        return self.__opener.open(url, data)
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def show(self):
        print self.__username
        print self.__password
        
a = Toy('aaa', 'nnn')
a.show()

