from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MVC.Controller.a import CommodityController


class Add_Commodity(object):

    def __init__(self, master):
        self.master = master

        # ===========Tao Title Add Commodity ============
        self.headingFrame1 = Frame(master, bg="#ff66f5", bd=5)
        self.headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.21)

        self.headingLabel = Label(self.headingFrame1, text="Add Commodity", bg='#fff5b5', fg='black',
                                  font=('Courier', 15))
        self.headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.labelFrame = Frame(master, bg='#6b81ff')
        self.labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

        cid = IntVar()
        name = StringVar()
        quantily = IntVar()
        price = DoubleVar()
        # ID
        self.com1 = Label(self.labelFrame, text="ID             : ", bg='#99ccff', fg='#004d99')
        self.com1.place(relx=0.05, rely=0.12, relheight=0.1)

        self.cInfo1 = Entry(self.labelFrame, textvariable=cid)
        self.cInfo1.place(relx=0.2, rely=0.12, relwidth=0.72, relheight=0.1)

        # Name
        self.com2 = Label(self.labelFrame, text="Name      : ", bg='#99ccff', fg='#004d99')
        self.com2.place(relx=0.05, rely=0.35, relheight=0.1)

        self.cInfo2 = Entry(self.labelFrame, textvariable=name)
        self.cInfo2.place(relx=0.2, rely=0.35, relwidth=0.72, relheight=0.1)

        # Quantily
        self.com3 = Label(self.labelFrame, text="Quantily  : ", bg='#99ccff', fg='#004d99')
        self.com3.place(relx=0.05, rely=0.57, relheight=0.1)

        self.cInfo3 = Entry(self.labelFrame, textvariable=quantily)
        self.cInfo3.place(relx=0.2, rely=0.57, relwidth=0.4, relheight=0.1)

        # Unit
        self.unit2 = Label(self.labelFrame, text="Unit : ", bg='#99ccff', fg='#004d99')
        self.unit2.place(relx=0.63, rely=0.57, relheight=0.1)

        self.cuInfo2 = ttk.Combobox(self.labelFrame)
        self.cuInfo2['value'] = ('kg', 'barrel')
        self.cuInfo2.place(relx=0.73, rely=0.57, relwidth=0.19, relheight=0.1)

        # Price
        self.com4 = Label(self.labelFrame, text="Price         :", bg='#99ccff', fg='#004d99')
        self.com4.place(relx=0.05, rely=0.8, relheight=0.1)

        self.cInfo4 = Entry(self.labelFrame, textvariable=price)
        self.cInfo4.place(relx=0.2, rely=0.8, relwidth=0.72, relheight=0.1)

        # Submit Button
        self.SubmitBtn = Button(master, text="SUBMIT", fg="Green", command=self.submit)
        self.SubmitBtn.place(relx=0.28, rely=0.86, relwidth=0.18, relheight=0.08)

        self.quitBtn = Button(master, text="Quit", fg="Red", command=master.destroy)
        self.quitBtn.place(relx=0.53, rely=0.86, relwidth=0.18, relheight=0.08)

    def submit(self):
        cid = self.cInfo1.get()
        cname = self.cInfo2.get()
        cquantily = self.cInfo3.get()
        cunit = self.cuInfo2.get()
        cprice = self.cInfo4.get()
        self.commodity1 = CommodityController(cid, cname, cquantily, cunit, cprice)
        if self.commodity1.getCID() == '':
            messagebox.showerror('Lỗi', 'Vui lòng nhập ID')
        elif self.commodity1.getCName() == '':
            messagebox.showerror('Lỗi', 'Vui lòng nhập Name')
        elif self.commodity1.getCQuantily() == '':
            messagebox.showerror('Lỗi', 'Vui lòng nhập Quantily')
        elif self.commodity1.getCPrice() == '':
            messagebox.showerror('Lỗi', 'Vui lòng nhập Price')
        else:
            Write_File = open('./../../Data/Data_Commodity.txt', 'a', encoding='utf-8')
            Write_File.write(cid + " " + cname + " " + cquantily + ' ' + cunit + ' ' + cprice)
            Write_File.write('\n')
            Write_File.close()
            self.cInfo1.delete(0, 'end')
            self.cInfo2.delete(0, 'end')
            self.cInfo3.delete(0, 'end')
            self.cInfo4.delete(0, 'end')


def main2():
    root = Tk()
    Add_Commodity(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=600)
    root.geometry("600x600")
    root.configure(bg='#88effc')
    root.mainloop()


if __name__ == "__main__":
    main2()
