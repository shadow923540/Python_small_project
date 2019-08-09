from tkinter import *

window = Tk()

label = Label(window, text="Welcome to tkinter")
text = Text(window, cnf={'bg': 'red'})
button = Button(window, text="Click Me!")


label.pack()
text.pack()
button.pack()


window.mainloop()



