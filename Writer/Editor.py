import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from datetime import datetime

import DataBase
from StyleAdder import styleWindow
import codecs

import Algoritms

class TxtEditor:

    def show_graphics(self):
        self.root.destroy()
        self.endTime = DataBase.endTime(self.FILE_NAME, self.startTime)
        self.diference = Algoritms.countOfWords(self.FILE_NAME) - self.countOfWords
        if self.diference < 0:
            self.diference = 0

        Algoritms.updateIgnoredWords(self.name)

        DataBase.addStats(self.FILE_NAME, Algoritms.indexCoolManual(self.FILE_NAME), Algoritms.tovtologic(self.FILE_NAME), Algoritms.productiv(self.startTime, self.endTime, self.diference))
        Algoritms.ShowGrafics(self.FILE_NAME, self.name)



    def new_file(self):
        self.FILE_NAME
        self.FILE_NAME = "Untitled"
        self.text.delete('1.0', tkinter.END)

    def save_file(self):
        data = self.text.get('1.0', tkinter.END)
        out = askopenfile(mode='w', defaultextension='txt')
        try:
            out.write(data.rstrip())
        except:
            showerror(title="Error", message="Saving file error")
        self.FILE_NAME = out.name
        if not self.isFileAdded:
            DataBase.addFileName(self.FILE_NAME)
            self.isFileAdded = True
        out.close()

    def save_as(self):
        out = asksaveasfile(mode='w', defaultextension='txt')
        data = self.text.get('1.0', tkinter.END)
        try:
            out.write(data.rstrip())
        except Exception:
            showerror(title="Error", message="Saving file error")
        self.FILE_NAME = out.name
        if not self.isFileAdded:
            DataBase.addFileName(self.FILE_NAME)
            self.isFileAdded = True


        out.close()

    def add_style(self):
        #self.root.destroy()
        self.stl = styleWindow(self.name)

    def open_file(self):

        with codecs.open(askopenfilename(filetypes=[("Text files","*.txt")]), encoding='utf-8') as inp:
            if inp is None:
                return
            self.FILE_NAME = inp.name
            if not self.isFileAdded:
                self.isFileAdded = True
                DataBase.addFileName(self.FILE_NAME)
            self.countOfWords = Algoritms.countOfWords(self.FILE_NAME)
            data = inp.read().encode('utf-8')
            self.text.delete('1.0', tkinter.END)
            self.text.insert('1.0', data)

    def info(self):
        self.messagebox.showinfo("Information", "Powered by Apik")


    def __init__(self, name):
        self.FILE_NAME = tkinter.NONE
        self.root = tkinter.Tk()
        self.name = name
        self.root.title(name)

        self.startTime = datetime.now()

        self.root.minsize(width=500, height=500)
        self.root.maxsize(width=500, height=500)
        self.text = tkinter.Text(self.root, width=400, height=400, font=("Arial", 15), wrap="word")
        self.scrollb = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.scrollb.pack(side="right", fill="y")
        self.text.configure(yscrollcommand=self.scrollb.set)

        self.isFileAdded = False

        self.countOfWords = 0

        self.text.pack()
        self.menuBar = tkinter.Menu(self.root)
        self.fileMenu = tkinter.Menu(self.menuBar)
        self.fileMenu.add_command(label="New", command=self.new_file)
        self.fileMenu.add_command(label="Open", command=self.open_file)
        self.fileMenu.add_command(label="Save", command=self.save_file)
        self.fileMenu.add_command(label="Save as", command=self.save_as)
        self.fileMenu.add_command(label="Style", command=self.add_style)

        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.menuBar.add_cascade(label="Exit", command=self.root.quit)
        self.root.config(menu=self.menuBar)

        self.root.protocol('WM_DELETE_WINDOW', self.show_graphics)
        self.root.mainloop()
