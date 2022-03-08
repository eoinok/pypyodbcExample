from tkinter import *
class TennisGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

                
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()

        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()

        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Enter your Date of Birth")
        self.label3.pack()

        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Enter your Member Type")
        self.label4.pack()

        self.entry4 = Entry()
        self.entry4.pack()
        
        self.insertButton = Button(master, text="Insert Into DB", command=self.hello)
        self.insertButton.pack()

        self.insertButton = Button(master, text="Print All Members", command=self.hello)
        self.insertButton.pack()
        
        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

    def hello(self):
        print("Your name is", self.entry1.get(), self.entry2.get())
        print("Your phone number is", self.entry3.get())

    def close(self):
        root.destroy()

root = Tk()
my_gui = TennisGUI(root)
root.dooneevent()
