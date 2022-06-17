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
roots = []
def compute():
    s = symbol_var.get()
    p = poly_var.get()
    g = guess_var.get().split(", ")
    i = iterations_var.get()
    reader = Reader(s)
    reader.read(p)
    poly_derivative = reader.poly_derivative()

    for val in g:
        resses = []
        root = newton(float(val), p.replace(s, "*"+s), poly_derivative, int(i), 0, resses)
        print(resses[-4:])
        print(resses)
        roots.append(root)
        for d in resses[-4:]:
           if (abs(root-d)) > 0.0001:
               roots.remove(root)
               break








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
ttk.Label(frm, text="Computed roots").grid(column=0, row=10)
ttk.Label(frm, text=roots.__str__()).grid(column=0, row=11)
root.mainloop()


