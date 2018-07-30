from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        dec = float(Decimal.get())
        value = 'b'
        while dec != 0:
            rem = dec%2
            dec = dec//2
        
            if rem == 0:
                value += str(0)
        
            else:
                value += str(1)
    
        value = value[1:]
        value = value[::-1]
        Binary.set(value)
    except ValueError:
        pass
    
root = Tk()
root.title("Decimal to Binary")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Decimal = StringVar()
Binary = StringVar()

decimal_entry = ttk.Entry(mainframe, width=7, textvariable=Decimal)
decimal_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=Binary).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Decimal").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Binary").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

decimal_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()