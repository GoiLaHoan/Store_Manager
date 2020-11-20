from tkinter import *
from MVC.View.Add_Commodity import main2
from MVC.View.View_Commodity import main3
from MVC.View.Payment import main4
from MVC.View.Edit_Commodity import main5
class MainWindow(object):
    def __init__(self, master):
        self.master = master

        self.headingFrame1 = Frame(master, bg="#ffd86e", bd=5)
        self.headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.21)

        self.headingLabel = Label(self.headingFrame1, text="My Store Mini", bg='#fff5b5', fg='black',
                                  font=('Courier', 24))
        self.headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.btn1 = Button(master, text="View All_Commodity", bg='#99ccff', fg='#004d99', command=main3)
        self.btn1.place(relx=0.275, rely=0.4, relwidth=0.45, relheight=0.1)

        self.btn2 = Button(master, text="Add Commodity", bg='#99ccff', fg='#004d99', command=main2)
        self.btn2.place(relx=0.275, rely=0.5, relwidth=0.45, relheight=0.1)

        self.btn3 = Button(master, text="Edit Commodity", bg='#99ccff', fg='#004d99', command=main5)
        self.btn3.place(relx=0.275, rely=0.6, relwidth=0.45, relheight=0.1)


        self.btn4 = Button(master, text="Payment", bg='#99ccff', fg='#004d99', command=main4)
        self.btn4.place(relx=0.275, rely=0.7, relwidth=0.45, relheight=0.1)


def main1():
    root = Tk()
    MainWindow(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=600)
    root.geometry("600x600")
    root.configure(bg='#88effc')
    root.mainloop()


if __name__ == "__main__":
    main1()
