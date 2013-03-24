#coding=utf8
from Tkinter import *
import Tkinter
import time
root = Tk()
class App:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		
		####################################
		w1 = Label(frame, text="a1")
		w1.pack()
		
		self.a1 = Entry(frame)
		self.a1.pack(padx=50)
		####################################
		w2 = Label(frame, text="a2")
		w2.pack()
		
		self.a2 = Entry(frame)
		self.a2.pack(padx=50)
		####################################
#		w4 = Label(frame, text="Symbol")
#		w4.pack()
#		
#		self.w4 = Entry(frame)
#		self.w4.pack(padx=50)
		####################################
		w3 = Label(frame, text="a1 + a2 = v1" )
		w3.pack()
		
		v1 = StringVar()
		e1 = Entry(frame, textvariable=v1)
		v1.set("")
		self.v1 = v1
		e1.pack()

		t = Button(frame, text="copy", command=self.t_copy)
		t.pack(side=RIGHT)
		
		b = Button(frame, text="Hello_list", command=self.hi)
		b.pack(side=RIGHT)
	
		e = Button(frame, text="exit", command=self.e_exit)
		e.pack(side=LEFT)

		cal_1 = Button(frame, text="+", command=self.caln_1)
		cal_1.pack(side=LEFT)
		cal_2 = Button(frame, text="-", command=self.caln_2)
		cal_2.pack(side=LEFT)
		cal_3 = Button(frame, text="*", command=self.caln_3)
		cal_3.pack(side=LEFT)
		cal_4 = Button(frame, text="/", command=self.caln_4)
		cal_4.pack(side=LEFT)
		
#		q1 = Button(frame, text="asd", command=self.q_1)
#		q1.pack()
#		q2 = Button(frame, text="2", command=self.q_1)
#		q2.pack(side=RIGHT)
#		q3 = Button(frame, text="3", command=self.q_1)
#		q3.pack(side=RIGHT)
#		q4 = Button(frame, text="4", command=self.q_1)
#		q4.pack(side=RIGHT)
#		q5 = Button(frame, text="5", command=self.q_1)
#		q5.pack(side=RIGHT)
#		q6 = Button(frame, text="6", command=self.q_1)
#		q6.pack(side=RIGHT)
#		q7 = Button(frame, text="7", command=self.q_1)
#		q7.pack(side=RIGHT)
#		q8 = Button(frame, text="8", command=self.q_1)
#		q8.pack(side=RIGHT)
#		q9 = Button(frame, text="9", command=self.q_1)
#		q9.pack(side=RIGHT)
#		q0 = Button(frame, text="0", command=self.q_1)
#		q0.pack(side=RIGHT)

#		Button(frame,text="1",command=lambda: callback(1)).grid(row=0,column=0)
#		Button(frame,text="2",command=lambda: callback(2)).grid(row=0,column=1)
#		Button(frame,text="3",command=lambda: callback(3)).grid(row=0,column=2)
#		Button(frame,text="4",command=lambda: callback(4)).grid(row=1,column=0)
#		Button(frame,text="5",command=lambda: callback(5)).grid(row=1,column=1)
#		Button(frame,text="6",command=lambda: callback(6)).grid(row=1,column=2)
#		Button(frame,text="7",command=lambda: callback(7)).grid(row=2,column=0)
#		Button(frame,text="8",command=lambda: callback(8)).grid(row=2,column=1)
#		Button(frame,text="9",command=lambda: callback(9)).grid(row=2,column=2)
		
		global number_list 
		self.number_list = []

		def changenum(number):
			self.number_list.append(number)
			print self.number_list
			
		num_1 = Button(root, text = '1', command = lambda: changenum(1))
		num_2 = Button(root, text = '2', command = lambda: changenum(2))
		num_3 = Button(root, text = '3', command = lambda: changenum(3))
		num_4 = Button(root, text = '4', command = lambda: changenum(4))
		num_5 = Button(root, text = '5', command = lambda: changenum(5))
		num_6 = Button(root, text = '6', command = lambda: changenum(6))
		num_7 = Button(root, text = '7', command = lambda: changenum(7))
		num_8 = Button(root, text = '8', command = lambda: changenum(8))
		num_9 = Button(root, text = '9', command = lambda: changenum(9))
		num_0 = Button(root, text = '0', command = lambda: changenum(0))

		js_1 = Button(root, text="+", command=self.caln_1)
		js_2 = Button(root, text="-", command=self.caln_2)
		js_3 = Button(root, text="*", command=self.caln_3)
		js_4 = Button(root, text="/", command=self.caln_4)
		js_5 = Button(root, text="=", command=self.caln_5)

		num_1.pack()
		num_2.pack()
		num_3.pack()
		num_4.pack()
		num_5.pack()
		num_6.pack()
		num_7.pack()
		num_8.pack()
		num_9.pack()
		num_0.pack()
		
		js_1.pack(side=LEFT)
		js_2.pack(side=LEFT)
		js_3.pack(side=LEFT)
		js_4.pack(side=LEFT)
		js_5.pack(side=LEFT)
		
		x1 = Label(root, text="x1")
		x1.pack()
		
		x1_v1 = StringVar()
		x1_e1 = Entry(root, textvariable=x1_v1)
		x1_v1.set("")
		self.x1_v1 = x1_v1
		x1_e1.pack()
		####################################
		x2 = Label(root, text="x2")
		x2.pack()
		
		x2_v1 = StringVar()
		x2_e1 = Entry(root, textvariable=x2_v1)
		x2_v1.set("")
		self.x2_v1 = x2_v1
		x2_e1.pack()
		####################################
		x3 = Label(root, text="=")
		x3.pack()
				
		x3_v1 = StringVar()
		x3_e1 = Entry(root, textvariable=x3_v1)
		x3_v1.set("")
		self.x3_v1 = x3_v1
		x3_e1.pack()
		
	def t_copy(self):
		n_a1 = self.a1.get()
		#n_a2 = self.a2.get()
		#re = int(n_a1) + int(n_a2)
		print self.v1.set(n_a1)

	def caln_1(self):
		caln_list_x1 = []
		if len(self.number_list) > 0:
			caln_list_x1 = self.x1_v1.set(self.number_list)
			self.number_list = []
			
	def caln_2(self):
		caln_list_x1 = []
		if len(self.number_list) > 0:
			caln_list_x1 = self.x1_v1.set(self.number_list)[:]
			self.number_list = []

	def caln_3(self):
		re = int(self.a1.get()) * int(self.a2.get())
		print self.v1.set(re)
	def caln_4(self):
		re = int(self.a1.get()) / int(self.a2.get())
		print self.v1.set(re)
	def caln_5(self):
		global caln_list_x1
		print self.x3_v1.set(caln_list_x1)

	def hi(self):
		print "v1 str",self.v1.get()
		print "a1 str",self.a1.get()
		print "a2 str",self.a2.get()
		#while True:
		#	time.sleep(1)
		#	pass
	def e_exit(self):
		print "exit..."
		exit()

app = App(root)
root.mainloop()
