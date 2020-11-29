from tkinter import *
from tkinter import messagebox
from MVC.View.View_Commodity import main1
from MVC.View.Payment import main4
from MVC.View.AddnEdit_Commodity import main3
from MVC.View.Graph import main5

class MainWindow(object):
    def __init__(self, master):
        self.master = master
        '''
        Design Heading Frame
        '''
        self.headingFrame = Frame(master, bg="#ffd86e", bd=5)
        self.headingFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.21)

        self.headingLb = Label(self.headingFrame, text="My Store Mini", bg='#fff5b5', fg='black',
                                  font=('Courier', 24))
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
    MainWindow(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=600)
    root.maxsize(width=600, height=600)
    root.geometry("600x600")
    root.configure(bg='#88effc')
    root.mainloop()

if __name__ == "__main__":
    mainwindow()


# '''
# Class Login
# '''
# class Login(object):
#     def __init__(self, master):
#         self.master = master
#
#         self.Frame_Login = Frame(self.master, height=200)
#         self.Frame_Login.pack(fill=X)
#         self.Label_Login = Label(self.Frame_Login, text="Welcome to Store Mini", fg='red', font="arial 20 bold")
#         self.Label_Login.place(relx=0.1, rely=0.02)
#         self.Label_User = Label(self.Frame_Login, text="Username: ", font=('time new roman', 17))
#         self.Label_User.place(relx=0.01, rely=0.3)
#         self.Label_Pass = Label(self.Frame_Login, text="Password: ", font=('time new roman', 17))
#         self.Label_Pass.place(relx=0.01, rely=0.55)
#
#         self.user = StringVar()
#         self.passw = StringVar()
#
#         self.Entry_User = Entry(self.Frame_Login, bg="white", bd=1,font=('Arial', 24), textvariable=self.user)
#         self.Entry_User.place(relx=0.3, rely=0.3, relwidth=0.6, relheight=0.15)
#         self.Entry_Pass = Entry(self.Frame_Login, bg="white", bd=1,font=('Arial', 24), show="*", textvariable=self.passw)
#         self.Entry_Pass.place(relx=0.3, rely=0.55, relwidth=0.6, relheight=0.15)
#
#         self.Btn_Login = Button(self.Frame_Login, text="Sign In",font=('Arial', 18), fg="Blue", command=self.Onclick)
#         self.Btn_Login.place(relx=0.25, rely=0.8, relwidth=0.3, relheight=0.15)
#         self.Btn_Cancel = Button(self.Frame_Login, text="Cancel",font=('Arial', 18), fg="Red", command=self.master.destroy)
#         self.Btn_Cancel.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.15)
#
#
#     '''
#     User and Password
#     '''
#     def Onclick(self, event=None):
#         UserName = self.Entry_User.get()
#         Passw = self.Entry_Pass.get()
#         if (UserName == "admin" and Passw == "admin"):
#             return self.Open_FrameMenu()
#         elif (UserName == "" or Passw == ""):
#             return messagebox.showerror("Error", "You have not entered full information")
#         else:
#             return messagebox.showerror("Error", "You entered incorrect account information")
#
#     def Open_FrameMenu(self):
#
#         self.master.destroy()
#         mainwindow()
#
#
#
# def main_Login():
#     Root_Login=Tk()
#     Login(Root_Login)
#     Root_Login.iconbitmap('shop.ico')
#     Root_Login.title("Mini Shop")
#     Root_Login.geometry("400x200")
#     Root_Login.resizable(False, False)
#     Root_Login.mainloop()
#
#
# if __name__ == "__main__":
#     main_Login()





