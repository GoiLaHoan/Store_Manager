from tkinter import *
from PIL import ImageTk
from MVC.View.View_Commodity import main1
from MVC.View.Payment import main4
from MVC.View.AddnEdit_Commodity import main3
from MVC.View.Graph import main5

class MainWindow(object):
    def __init__(self, master):
        self.master = master

        # Add Icon
        self.view_icon = ImageTk.PhotoImage(file="images/find.png")
        self.payment_icon = ImageTk.PhotoImage(file="images/bill.png")
        self.graph_icon = ImageTk.PhotoImage(file="images/graph.png")
        self.update_icon = ImageTk.PhotoImage(file="images/update.png")

        # Design Background
        self.bg = ImageTk.PhotoImage(file="images/bg1.jpg")
        self.bg_image = Label(self.master, image=self.bg).pack()


        '''
        Design Heading Frame
        '''
        # self.headingFrame = Frame(master, bg="#ffd86e", bd=5)
        # self.headingFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.21)
        #
        # self.headingLb = Label(self.headingFrame, text="My Store Mini", bg='#fff5b5', fg='black',
        #                           font=('arial bold', 24))
        # self.headingLb.place(relx=0, rely=0, relwidth=1, relheight=1)

        '''
        Design Button
        '''
        #Button View
        self.btnView = Button(master, text="View All_Commodity", image=self.view_icon,compound=TOP, fg='#004d99',bd=3, command=main1)
        self.btnView.place(relx=0.1, rely=0.77, relwidth=0.2, relheight=0.2)

        #Button Add/Edit
        self.btnEdit = Button(master, text="Add/Edit Commodity", image=self.update_icon,compound=TOP, fg='#004d99',bd=3, command=main3)
        self.btnEdit.place(relx=0.31, rely=0.77, relwidth=0.2, relheight=0.2)

        #Button Payment
        self.btnPayment = Button(master, text="Payment", image=self.payment_icon,compound=TOP, fg='#004d99',bd=3, command=main4)
        self.btnPayment.place(relx=0.52, rely=0.77, relwidth=0.2, relheight=0.2)

        #Button Graph
        self.btnGraph = Button(master, text="Graph", image=self.graph_icon,compound=TOP, fg='#004d99',bd=3, command=main5)
        self.btnGraph.place(relx=0.73, rely=0.77, relwidth=0.2, relheight=0.2)

def mainwindow():
    root = Tk()
    obj=MainWindow(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=500)
    root.maxsize(width=600, height=500)
    # root.geometry("600x600")
    # root.configure(bg='#c7f9ff')
    root.mainloop()

if __name__ == "__main__":
    mainwindow()

