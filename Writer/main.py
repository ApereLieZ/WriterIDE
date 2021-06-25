import tkinter as tk
from Editor import TxtEditor
import DataBase as db
class startWindow:


    def __init__(self, w, h,name):

        self.startWindow = tk.Tk()
        self.screenw = self.startWindow.winfo_screenwidth()
        self.screenh = self.startWindow.winfo_screenheight()
        self.startWindow.title(name)
        self.width = w
        self.height = h
        self.userName = tk.StringVar()

        self.startWindow.geometry(f"{self.width}x{self.height}+{str(int(self.screenw/2 - self.width/2))}+{str(int(self.screenh/2-self.height/2))}")
        self.startWindow.resizable(False, False)
        self.mainLabel = tk.Label(self.startWindow,
                                  text = "Input Login",
                                  font=("Arial", 20, "bold")).place(x = self.width /3, y = 10)

        self.txtField = tk.Entry(self.startWindow,
                                 width = 22,
                                 font=("Arial", 20),
                                 textvariable=self.userName).place(x = self.width/2-150, y = 75)

        self.btnLog = tk.Button(self.startWindow,
                                text = "Log In",
                                font=("Arial", 20, "bold"),
                                command = self.findUser).place(x = self.width/2-150, y = 150)
        self.btnReg = tk.Button(self.startWindow,
                                text = "Register",
                                font=("Arial", 20, "bold"),
                                command = self.regUser).place(x = self.width/2+50, y = 150)

        self.errLabel = tk.Label(self.startWindow,
                                  text = "",
                                  fg = "red",
                                  font=("Arial", 20, "bold"))
        self.errLabel.pack(side = tk.BOTTOM)
        self.startWindow.mainloop()

    def findUser(self):
        if(db.getUser(self.userName.get())):
            self.startWindow.destroy()
            a = TxtEditor(self.userName.get())

        else:

            self.errLabel['text'] = f'User {self.userName.get()} not registered'
            self.userName.set("")

    def regUser(self):
        if(db.addUser(self.userName.get())):
            self.startWindow.destroy()
            a = TxtEditor(self.userName.get())
        else:

            self.errLabel['text'] = f'User {self.userName.get()} is exist'
            self.userName.set("")

def main():
    win = startWindow(500,300, "StartMenu")

main()