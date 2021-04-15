
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.configure(background='pink1')
class Widgets:
    def __init__(self, main_widget):
        self.main_widget = main_widget
        main_widget.title("Task Manager")
        self.bg = "PaleTurquoise1"
        self.text = 'Label'
        self.widget = ''
        self.width = 15
        self.fg = 'green'
        main_widget.geometry("750x400")

    def set_name(self, name, r, c):
        self.widget = tkinter.Label(self.main_widget, text=name, bg="pink1")
        self.widget.grid(row=r, column=c)

    def input_text(self):
        self.widget = tkinter.Entry(self.main_widget, width=self.width)
        self.widget.grid(row=2, column=1)


    def display_button(self, txt, command, r, c):
        self.widget = tkinter.Button(root, text=txt, bg=self.bg, command=command)
        self.widget.grid(row=r, column=c)

    def task_box(self):
        self.widget = tkinter.Listbox(root)
        self.widget.grid(row=0, column=1, rowspan=3)

    def alert(self, title, message):
        self.widget = tkinter.messagebox.showwarning(title, message)

    def inform(self, title, message):
        self.widget=tkinter.messagebox.showinfo(title, message)

