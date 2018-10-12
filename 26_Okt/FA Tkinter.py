from tkinter import *
from NS import ns

root = Tk()
lijst = ['0','0','0','0','0']
def Toon_FirstFrame():
    SecondFrame.pack_forget()
    FirstFrame.pack()

def Toon_SecondFrame():
    SecondFrame.pack()
    station = StationVeld.get()
    global lijst
    lijst = ns(station)
    Trein1['text'] = lijst[0]
    Trein2['text'] = lijst[1]
    Trein3['text'] = lijst[2]
    Trein4['text'] = lijst[3]
    Trein5['text'] = lijst[4]
    Trein1.pack()
    Trein2.pack()
    Trein3.pack()
    Trein4.pack()
    Trein5.pack()
    FirstFrame.pack_forget()
    BackButton.pack()

FirstFrame = Frame(master=root)
FirstFrame.pack(fill='both',expand=True)
SecondFrame = Frame(master=root)
SecondFrame.pack(fill='both', expand=True)
StationVeld = Entry(master=FirstFrame)
StationVeld.pack(padx=20,pady=20)
ConfirmButton = Button(master=FirstFrame, text='Go', command=Toon_SecondFrame)
ConfirmButton.pack()
Trein1 = Label(master=SecondFrame, text=lijst[0])
Trein2 = Label(master=SecondFrame, text=lijst[1])
Trein3 = Label(master=SecondFrame, text=lijst[2])
Trein4 = Label(master=SecondFrame, text=lijst[3])
Trein5 = Label(master=SecondFrame, text=lijst[4])
BackButton = Button(master=SecondFrame, text='Back', command=Toon_FirstFrame)

root.mainloop()