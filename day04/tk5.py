#coding=utf8
from Tkinter import *
import Tkinter
import time
root = Tk()

class App:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		
		e = Button(frame, text="exit", command=self.e_exit)
		
		global caln_list_x1
		global number_list
		self.number_list = []

		def changenum(number):
			print self.number_list
			if self.x4_v1.get() == "":
				self.number_list.append(str(number))
				self.x1_v1.set(''.join(self.number_list))
			if self.x4_v1.get() != "":
				self.number_list.append(str(number))
				self.x2_v1.set(''.join(self.number_list))
		####################################
		x1 = Label(frame, text="v1")
		x1.pack()
		
		x1_v1 = StringVar()
		x1_e1 = Entry(frame, textvariable=x1_v1)
		x1_v1.set("")
		self.x1_v1 = x1_v1
		x1_e1.pack()
		####################################
		x2 = Label(frame, text="x2")
		x2.pack()
		
		x2_v1 = StringVar()
		x2_e1 = Entry(frame, textvariable=x2_v1)
		x2_v1.set("")
		self.x2_v1 = x2_v1
		x2_e1.pack()
		####################################
		x3 = Label(frame, text="=")
		x3.pack()
				
		x3_v1 = StringVar()
		x3_e1 = Entry(frame, textvariable=x3_v1)
		x3_v1.set("")
		self.x3_v1 = x3_v1
		x3_e1.pack()
		####################################
		x4_v1 = StringVar()
		x4_e1 = Entry(frame, textvariable=x4_v1)
		x4_v1.set("")
		self.x4_v1 = x4_v1
		x4_e1.pack()

		num_1 = Button(frame, text = '1', command = lambda: changenum(1))
		num_2 = Button(frame, text = '2', command = lambda: changenum(2))
		num_3 = Button(frame, text = '3', command = lambda: changenum(3))
		num_4 = Button(frame, text = '4', command = lambda: changenum(4))
		num_5 = Button(frame, text = '5', command = lambda: changenum(5))
		num_6 = Button(frame, text = '6', command = lambda: changenum(6))
		num_7 = Button(frame, text = '7', command = lambda: changenum(7))
		num_8 = Button(frame, text = '8', command = lambda: changenum(8))
		num_9 = Button(frame, text = '9', command = lambda: changenum(9))
		num_0 = Button(frame, text = '0', command = lambda: changenum(0))

		js_1 = Button(frame, text="+", command=self.caln_1)
		js_2 = Button(frame, text="-", command=self.caln_2)
		js_3 = Button(frame, text="*", command=self.caln_3)
		js_4 = Button(frame, text="/", command=self.caln_4)
		js_5 = Button(frame, text="=", command=self.caln_5)
		
		js_1.pack(side=LEFT)
		js_2.pack(side=LEFT)
		js_3.pack(side=LEFT)
		js_4.pack(side=LEFT)
		js_5.pack(side=LEFT)

		num_1.grid(row=0,column=0)
		num_1.pack()
		num_2.grid(row=0,column=1)
		num_2.pack()
		num_3.grid(row=0,column=2)
		num_3.pack()
		num_4.grid(row=1,column=0)
		num_4.pack()
		num_5.grid(row=1,column=0)
		num_5.pack()
		num_6.grid(row=1,column=2)
		num_6.pack()
		num_7.grid(row=2,column=0)
		num_7.pack()
		num_8.grid(row=2,column=1)
		num_8.pack()
		num_9.grid(row=2,column=2)
		num_9.pack()
		num_0.grid(row=0,column=0)
		num_0.pack()
		

		e.pack(side=LEFT)

	def get_Number(self, Symb):
		self.x4_v1.set(Symb)
		if len(self.number_list) > 0:
			self.x1_v1.set(''.join(self.number_list))
			self.number_list = []
			
	def caln_1(self):
		dengyu = "+"
		self.get_Number(dengyu)
	def caln_2(self):
		dengyu = "-"
		self.get_Number(dengyu)
	def caln_3(self):
		dengyu = "*"
		self.get_Number(dengyu)
	def caln_4(self):
		dengyu = "/"
		self.get_Number(dengyu)

	def Calc(self, Value_1, Value_2, Symbol):
		if Symbol == "+":
			Value_3 = Value_1 + Value_2
		elif Symbol == "-":
			Value_3 = Value_1 - Value_2
		elif Symbol == "*":
			Value_3 = Value_1 * Value_2
		elif Symbol == "/":
			Value_3 = Value_1 / Value_2
			
		Value_re = "%d %s %d = %d" %(Value_1, Symbol, Value_2, Value_3)
		self.x3_v1.set(Value_re)
		
	def caln_5(self):

		if len(self.number_list) > 0:
			self.x2_v1.set(''.join(self.number_list))
			self.number_list = []

		Symbol = self.x4_v1.get()
		print Symbol
		Value_1 = int(self.x1_v1.get())
		Value_2 = int(self.x2_v1.get())
		
		self.Calc(Value_1, Value_2, Symbol)

		self.x3_v1.get()
	
		self.x1_v1.set("")
		self.x2_v1.set("")
		self.x4_v1.set("")
		self.number_list = []

	def e_exit(self):
		print "exit..."
		exit()

app = App(root)
root.mainloop()
