from tkinter import * 
from tkinter import messagebox

a = Tk()
a.geometry("600x600")
a.title("Classes")

class CreateElements:
    def __init__(self):
        print("This is Create Elements Class")
    def CreateNewElement(self):
        l1 = Label(a, text = "A New Label Has Been Created Using Class", fg = "green")
        b1 = Button(a, text = " Button ", command = self.message)
        l1.pack()
        b1.pack(padx = 20, pady = 10)
    def message(self):
        messagebox.showinfo("Info", "You Clicked The Button Created Using Class")
    

o1 = CreateElements()

b2 = Button(a, text = "Click To Create Label And Button Element", command = o1.CreateNewElement)
b2.pack(padx = 20, pady = 10)

a.mainloop()