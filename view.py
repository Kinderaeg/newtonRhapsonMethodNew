import tkinter
from tkinter import *
from tkinter import ttk
from reader import *
from main import *
root = Tk()
symbol_var = tkinter.StringVar()
poly_var = tkinter.StringVar()
guess_var = tkinter.StringVar()
iterations_var = tkinter.StringVar()
def compute():
    s = symbol_var.get()
    p = poly_var.get()
    g = guess_var.get().split(", ")
    i = iterations_var.get()
    reader = Reader(s)
    reader.read(p)
    poly_derivative = reader.poly_derivative()

    roots = []
    for val in g:
       roots.append(newton(val, p, poly_derivative, i, 0))
    return roots


print(roots)

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Input symbol (x,t,r etc.)").grid(column=0, row=0)
ttk.Entry(frm, textvariable=symbol_var).grid(column=0,row=1)
ttk.Label(frm, text="Input polynomial").grid(column=0, row=2)
ttk.Entry(frm, textvariable=poly_var).grid(column=0,row=3)
ttk.Label(frm, text="Input guesses").grid(column=0, row=4)
ttk.Entry(frm, textvariable=guess_var).grid(column=0,row=5)
ttk.Label(frm, text="Input iterations").grid(column=0, row=6)
ttk.Entry(frm, textvariable=iterations_var).grid(column=0,row=7)
ttk.Label(frm, text="Computing root").grid(column=0, row=8)
ttk.Button(frm, text="Compute", command=compute).grid(column=0, row=9)
root.mainloop()


