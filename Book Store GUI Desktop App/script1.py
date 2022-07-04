"""
A progream that stores the following book information:
    - Title, Author, Year, ISBN

A user can perform the following actions:
    - View all records
    - Search an entry
    - Add an entry
    - Update an entry
    - Delete a record
    - Close the app

"""

from lib2to3.pgen2 import grammar
from tkinter import *
import tkinter

window = Tk()


def km_to_miles():
    # print(e1_value.get())
    gram = float(e1_value.get()) * 1000.0
    lb = float(e1_value.get()) * 2.20462
    oz = float(e1_value.get()) * 35.274

    r1.delete('1.0', END)
    r1.insert(END, gram)

    r2.delete('1.0', END)
    r2.insert(END, lb)

    r3.delete('1.0', END)
    r3.insert(END, oz)


l1 = Label(window, text='Kg')
l1.grid(row=0, column=0)

b1 = Button(window, text='Convert', command=km_to_miles)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

r1 = Text(window, height=1, width=20)
r1.grid(row=1, column=0)

r2 = Text(window, height=1, width=20)
r2.grid(row=1, column=1)

r3 = Text(window, height=1, width=20)
r3.grid(row=1, column=2)


# keeps the window open
window.mainloop()
