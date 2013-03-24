num = 0
print num
def changenum(newnum):
    global num
    num = newnum
    print num

import Tkinter

top = Tkinter.Tk()
num_1 = Tkinter.Button(top, text = '1', command = lambda: changenum(1))
num_2 = Tkinter.Button(top, text = '2', command = lambda: changenum(2))

num_1.pack()
num_2.pack()

print 
Tkinter.mainloop()
