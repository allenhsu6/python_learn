#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameIput = Entry(self)
        self.nameIput.pack()
        self.alertbutton = Button(self, text='请输入您的名字', command=self.box)
        self.alertbutton.pack()

    def box(self):
        name = self.nameIput.get() or '为什么不写名？？'
        messagebox.showinfo('欢迎界面', 'Hello, %s' % name)

app = Application()
app.master.title('my first GUI')
app.mainloop()



