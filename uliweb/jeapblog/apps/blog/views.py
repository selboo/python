#coding=utf-8
from uliweb import expose
from blog.forms import blogform
from blog.models import blogm

@expose('/')
def index():
	f = blogform(action='/blog')
	blogm_all = blogm.all()
	return {'f':f,'blogm_all':blogm_all}

@expose('/blog/<name>/<age>/')
def index(name,age):
	if request.method == 'POST':
		for i in request.params.keys():
			print i,request.params[i]
		n         = blogm()
		n.name    = request.params["name"]
		n.content = request.params["content"]
		n.save()

	blog = blogform()
	blogm_all = blogm.all()
	return {"name":name,"age":age,'blog':blog,"blogm_all":blogm_all}

@expose('/sum/<name>/<aa>')
def sum(name,aa):
    c = int(name) + int(aa)
    return '<h1>Hello, Uliweb %d  </h1>' % c

@expose('/test')
def test():
        for i in request.params.keys():
                print request.params[i]
        return {}

