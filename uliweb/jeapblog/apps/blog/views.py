#coding=utf-8
from uliweb import expose
from blog.forms import blogform
from blog.models import blogm

@expose('/')
def index():
	form = blogform(action='/save')
	blogm_all = blogm.all()
	return {'form':form,'blogm_all':blogm_all}

@expose('/save')
def index_save():
	form = blogform()
	
	if hasattr(request, 'user') and request.user:
		pass
	else:
		return redirect('/alert')

	if request.method == 'POST':
		flag = form.validate(request.params)
		if flag:
			n      = blogm(**form.data)
			n.name = request.user.username
			n.save()
	
	
#	for i in request.params.keys():
#		print request.params[i]
#	return {}

	return redirect('/')

@expose('/delete/<ida>')
def index_delete(ida):
	form = blogform()
	
	if hasattr(request, 'user') and request.user:
		pass
	else:
		return redirect('/login')
	
	if request.method == 'GET':
		n = blogm()
		n.filter(n.c.id==ida).remove()
		
	return redirect('/')

@expose('/alert')
def index_alert():
	return { }


@expose('/edit/<id>')
def edit(id):
	blogs = functions.get_model('blogm')
	if request.method == 'GET':
		p = blogm.get(blogs.c.id==id)
		form = blogform(data = p.to_dict(),action="/update/%s" %id)
		print form
		return {'form':form}
#	elif request.method == 'POST':
#		form = blogform()
#		flag = form.validate(request.params)
#		n = blogm.get(blogm.c.id == id)
#		if n:
#			n.username = request.user.username
#			n.title    = form.data.title
#			n.content  = form.data.content
#			n.save()
#		return redirect('/');

@expose('/update/<id>')
def update(id):
	form = blogform()
	flag = form.validate(request.params)
	n = blogm.get(blogm.c.id == id)
	if n:
		n.id       = id
		n.name     = request.user.username
		n.title    = form.data.title
		n.content  = form.data.content
		n.save()
		
#		n.id   = id
#		n.name = request.user.username
#		n      = blogm(**form.data)
#		n.save()

	return redirect('/');
	
@expose('/blog')
def index1():
#	blogs = functions.get_model('blogm')
#	blog = blogs.all()

	form = blogform()

	if request.method == 'POST':
		for i in request.params.keys():
			print i,request.params[i]
#		n         = blogm()
#		n.name    = request.params["name"]
#		n.content = request.params["content"]
#		n.save()
		flag = form.validate(request.params)
		if flag:
			n = blogm(**form.data)
			n.save()

	blog_all = blogform()
	blogm_all = blogm.all()
	return {"blog":blog_all,"blogm_all":blogm_all}
	#return {"name":name,"age":age,"blog":blog_all,"blogm_all":blogm_all}

@expose('/blog/save')
def test():
	for i in request.params.keys():
		print request.params[i]
	return {}

#@expose('/sum/<name>/<aa>')
#def sum(name,aa):
#	c = int(name) + int(aa)
#	return '<h1>Hello, Uliweb %d  </h1>' % c
#
#@expose('/test')
#def test():
#	for i in request.params.keys():
#		print request.params[i]
#	return {}

