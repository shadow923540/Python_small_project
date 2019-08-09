from tkinter import *


def doOK():
    print("OK button clicked")

def doCancel():
    print("Cancel button clicked")

window = Tk()

btnOK = Button(window, text="OK", fg='blue',
               command=doOK)
btnCancel = Button(window, text="Cancel", bg='blue',
               command=doCancel)

btnOK.grid(row=1, column=1, padx= (2,10), pady=5) #other method then pack
btnCancel.place(x=72, y=5)       #You can't mix grid and pack, but you can with place



window.mainloop()