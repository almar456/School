from tkinter import *
root = Tk()

button1 = Button(master=root, text='Button 1')
button1.place(x=10, y=30)

button2 = Button(master=root, text='Button 2')
button2.place(x=10, y=60)

button3 = Button(master=root, text='Button 3')
button3.place(x=50, y=45)

root.mainloop()