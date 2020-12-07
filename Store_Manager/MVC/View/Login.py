from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from MVC.View.MainWindow import mainwindow
class Login(object):
    def __init__(self, master):
        self.master = master

        '''
        Design Heading Frame
        '''
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon = ImageTk.PhotoImage(file="images/man-user.png")
        self.pass_icon = ImageTk.PhotoImage(file="images/pw.png")
        self.avatar_icon = ImageTk.PhotoImage(file="images/avatar.png")

        self.bg_image = Label(self.master, image=self.bg).pack()

        #======variables=========
        self.username=StringVar()
        self.pw=StringVar()

        '''
        Design Login Frame
        '''
        Login_Frame=Frame(self.master, bg='#88effc')
        Login_Frame.place(x=160,y=70)

        avatar_Lb=Label(Login_Frame, image=self.avatar_icon,bg='#88effc',bd=1)
        avatar_Lb.grid(row=0,columnspan=2,pady=20)

        user_Lb=Label(Login_Frame, text='Username',bg='#88effc', image=self.user_icon,compound=LEFT, font=('time new roman', 12,'bold'))
        user_Lb.grid(row=1,column=0,padx=0,pady=7)
        txtuser=Entry(Login_Frame,textvariable=self.username,relief=GROOVE)
        txtuser.grid(row=1,column=1,padx=35)

        pw_Lb=Label(Login_Frame, text='Password',bg='#88effc', image=self.pass_icon,compound=LEFT, font=('time new roman', 12,'bold'))
        pw_Lb.grid(row=2,column=0,padx=0,pady=7)
        txtpw = Entry(Login_Frame,textvariable=self.pw, relief=GROOVE, show='*')
        txtpw.grid(row=2, column=1,padx=35)

        '''
        Design Button
        '''
        btn_exit = Button(Login_Frame, text='Exit', width=15, font=('time new roman', 10, 'bold'), fg='red',command=self.master.destroy)
        btn_exit.grid(row=3, column=0, pady=10)

        btn_login=Button(Login_Frame,text='Login', width=15,font=('time new roman', 10,'bold'),fg='green', command=self.login)
        btn_login.grid(row=3,column=1,pady=10)

    #Function Login
    def login(self):
        if self.username.get()=='' or self.pw.get()=='':
            messagebox.showerror("Error", 'All files are required!')
        elif self.username.get()=='admin' or self.pw.get()=='admin':
            messagebox.showinfo('Successfull',f'welcome {self.username.get()}')
            return self.Open_FrameMenu()
        else:
            messagebox.showerror("Error", 'Invalid Username or Password')

    def Open_FrameMenu(self):

        self.master.destroy()
        mainwindow()

def mainlogin():
    root = Tk()
    Login(root)
    root.title("Login")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=500)
    root.maxsize(width=600, height=500)
    root.mainloop()


if __name__ == "__main__":
    mainlogin()
