from tkinter import *
from PIL import ImageTk
from MVC.View.View_Commodity import main1
from MVC.View.Payment import main4
from MVC.View.AddnEdit_Commodity import main3
from MVC.View.Graph import main5

class MainWindow(object):
    def __init__(self, master):
        self.master = master

        # Design Background
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        self.bg_image = Label(self.master, image=self.bg).pack()


        '''
        Design Heading Frame
        '''
        self.headingFrame = Frame(master, bg="#ffd86e", bd=5)
        self.headingFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.21)

        self.headingLb = Label(self.headingFrame, text="My Store Mini", bg='#fff5b5', fg='black',
                                  font=('arial bold', 24))
        self.headingLb.place(relx=0, rely=0, relwidth=1, relheight=1)

        '''
        Design Button
        '''
        #Button View
        self.btnView = Button(master, text="View All_Commodity", bg='#99CCFF', fg='#004d99', command=main1)
        self.btnView.place(relx=0.275, rely=0.4, relwidth=0.45, relheight=0.1)

        #Button Add/Edit
        self.btnEdit = Button(master, text="Add/Edit Commodity", bg='#99ccff', fg='#004d99', command=main3)
        self.btnEdit.place(relx=0.275, rely=0.5, relwidth=0.45, relheight=0.1)

        #Button Payment
        self.btnPayment = Button(master, text="Payment", bg='#99ccff', fg='#004d99', command=main4)
        self.btnPayment.place(relx=0.275, rely=0.6, relwidth=0.45, relheight=0.1)

        #Button Graph
        self.btnGraph = Button(master, text="Graph", bg='#99ccff', fg='#004d99', command=main5)
        self.btnGraph.place(relx=0.275, rely=0.7, relwidth=0.45, relheight=0.1)

def mainwindow():
    root = Tk()
    obj=MainWindow(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=500)
    root.maxsize(width=600, height=500)
    # root.geometry("600x600")
    # root.configure(bg='#88effc')
    root.mainloop()

if __name__ == "__main__":
    mainwindow()

