"""coding: utf-8"""

import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir Navegador')
root.geometry('300x200')


def google():
    webbrowser.open('www.google.com')


mygoogle = Button(root, text='Abrir Google', command=google).pack(pady=20)
root.mainloop()
