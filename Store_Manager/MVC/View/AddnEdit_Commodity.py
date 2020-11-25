from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF
from MVC.Controller.Commodity_Controller import CommodityController

class Edit_Commodity(object):

    def __init__(self, master):
        self.master = master
        self.checkclickshow = False

        '''
        Create Heading Edit Commodity
        '''
        self.Heading_Edit = Frame(master, bg="#ff66f5", bd=5)
        self.Heading_Edit.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.18)

        self.headingLb = Label(self.Heading_Edit, text="Edit Commodity", bg='#fff5b5', fg='black',
                               font=('Courier', 15))
        self.headingLb.place(relx=0, rely=0, relwidth=1, relheight=1)

        '''
            Create Frame Search ID
        '''
        self.SearchID_Frame = Frame(master, bg='#6b81ff')
        self.SearchID_Frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.05)

        self.SearchID_Label = Label(self.SearchID_Frame, text="Search ID: ", bg='#6b81ff', fg='white')
        self.SearchID_Label.place(relx=0.05, rely=0.2)

        self.SearchID_Entry = Entry(self.SearchID_Frame)
        self.SearchID_Entry.place(relx=0.2, rely=0.2, relwidth=0.72)

        '''
            Create Listbox Data
        '''
        self.listbox = Listbox(master, width=55, height=1, font=('arial', 12, 'bold'))
        self.listbox.place(relx=0.1, rely=0.32, relwidth=0.8, relheight=0.05)
        self.listbox.bind('<<ListboxSelect>>', self.onClick)

        # ======================================
        self.cid = IntVar()
        self.name = StringVar()
        self.unit = StringVar()
        self.quantily = IntVar()
        self.price = DoubleVar()
        # ======================================

        '''
            Design FrameEdit
        '''
        self.labelFrame = Frame(master, bg='#6b81ff')
        self.labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

        # ID
        self.ID_Label = Label(self.labelFrame, text="ID             : ", bg='#99ccff', fg='#004d99')
        self.ID_Label.place(relx=0.05, rely=0.12, relheight=0.1)

        self.ID_Entry = Entry(self.labelFrame, textvariable=self.cid)
        self.ID_Entry.place(relx=0.2, rely=0.12, relwidth=0.72, relheight=0.1)

        # Name
        self.Name_Label = Label(self.labelFrame, text="Name      : ", bg='#99ccff', fg='#004d99')
        self.Name_Label.place(relx=0.05, rely=0.35, relheight=0.1)

        self.Name_Entry = Entry(self.labelFrame, textvariable=self.name)
        self.Name_Entry.place(relx=0.2, rely=0.35, relwidth=0.72, relheight=0.1)

        # Quantily
        self.Quantily_Label = Label(self.labelFrame, text="Quantily  : ", bg='#99ccff', fg='#004d99')
        self.Quantily_Label.place(relx=0.05, rely=0.57, relheight=0.1)

        self.Quantily_Entry = Entry(self.labelFrame, textvariable=self.quantily)
        self.Quantily_Entry.place(relx=0.2, rely=0.57, relwidth=0.4, relheight=0.1)

        # Unit
        self.Unit_Label = Label(self.labelFrame, text="Unit : ", bg='#99ccff', fg='#004d99')
        self.Unit_Label.place(relx=0.63, rely=0.57, relheight=0.1)

        self.Unit_Entry = ttk.Combobox(self.labelFrame, textvariable=self.unit)
        self.Unit_Entry['value'] = ('kg', 'barrel')
        self.Unit_Entry.place(relx=0.73, rely=0.57, relwidth=0.19, relheight=0.1)

        # Price
        self.Price_Label = Label(self.labelFrame, text="Price         :", bg='#99ccff', fg='#004d99')
        self.Price_Label.place(relx=0.05, rely=0.8, relheight=0.1)

        self.Price_Entry = Entry(self.labelFrame, textvariable=self.price)
        self.Price_Entry.place(relx=0.2, rely=0.8, relwidth=0.72, relheight=0.1)

        '''
        Design Button
        '''



        # View Button
        self.ViewBtn = Button(master, text="SHOW", fg="Orange", command=self.show)
        self.ViewBtn.place(relx=0.06, rely=0.86, relwidth=0.18, relheight=0.08)

        # Add Button
        self.AddBtn = Button(master, text="ADD", fg="Blue", command=self.submit)
        self.AddBtn.place(relx=0.28, rely=0.86, relwidth=0.18, relheight=0.08)

        # Update Button
        self.UpdateBtn = Button(master, text="UPDATE", fg="Green", command=self.update)
        self.UpdateBtn.place(relx=0.50, rely=0.86, relwidth=0.18, relheight=0.08)

        # Quit Button
        self.QuitBtn = Button(master, text="Quit", fg="Red", command=master.destroy)
        self.QuitBtn.place(relx=0.72, rely=0.86, relwidth=0.18, relheight=0.08)

    def update(self):
        if self.checkclickshow:
            f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'r+')
            d = f.readlines()
            listE = []
            f.seek(0)

            # Create object
            cid = self.ID_Entry.get()
            cname = self.Name_Entry.get()
            cquantily = self.Quantily_Entry.get()
            cunit = self.Unit_Entry.get()
            cprice = self.Price_Entry.get()
            self.Edit_Commodity = CommodityController(cid, cname, cquantily, cunit, cprice)


            for w in d:
                line = w.split()
                listE.append(line)
            for i in range(len(d)):
                if self.SearchID_Entry.get() == listE[i][0]:
                    d[i] = d[i].replace(listE[i][0], self.Edit_Commodity.getCID(), 1)
                    d[i] = d[i].replace(listE[i][1], self.Edit_Commodity.getCName(), 1)
                    d[i] = d[i].replace(listE[i][2], self.Edit_Commodity.getCQuantily(), 1)
                    d[i] = d[i].replace(listE[i][3], self.Edit_Commodity.getCUnit(), 1)
                    d[i] = d[i].replace(listE[i][4], self.Edit_Commodity.getCPrice(), 1)
                f.write(d[i])
            f.truncate()
            f.close()

            # Delete all the entry content
            self.ID_Entry.delete(0, 'end')
            self.Name_Entry.delete(0, 'end')
            self.Quantily_Entry.delete(0, 'end')
            self.Price_Entry.delete(0, 'end')
            self.SearchID_Entry.delete(0, 'end')
            self.listbox.delete(0, 'end')
            self.Unit_Entry.delete(0, 'end')

            messagebox.showinfo("Done", "You have successfully updated")
            self.checkclickshow = False
        else:
            messagebox.showerror('Error', 'You need to click on ''SHOW'' first')


    def show(self):
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        listC = []
        self.listbox.delete(0, END)
        for line in f:
            line = line.split()
            listC.append(line)
        flag = False
        for i in range(len(listC)):
            if self.SearchID_Entry.get() == listC[i][0]:
                self.listbox.insert(END, listC[i])
                flag=True
        if flag == False:
            messagebox.showinfo('dsdsd', 'ID chưa có, bạn muốn thêm vào cửa hàng không?')
        f.close()


    # Transfers the data into entries
    def onClick(self, event):
        pd = self.listbox.get(ACTIVE)

        self.ID_Entry.delete(0, END)
        self.ID_Entry.insert(END, pd[0])

        self.Name_Entry.delete(0, END)
        self.Name_Entry.insert(END, pd[1])

        self.Quantily_Entry.delete(0, END)
        self.Quantily_Entry.insert(END, pd[2])

        self.Unit_Entry.delete(0, END)
        self.Unit_Entry.insert(END, pd[3])

        self.Price_Entry.delete(0, END)
        self.Price_Entry.insert(END, pd[4])

        self.checkclickshow = True


# Check the ID is the same or not?
    def checkID(self, CID):
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        for line in f:
            line = line.split()
            if CID == line[0]:
                return False
        return True

    #Function Submit
    def submit(self):

        # Create object
        cid = self.ID_Entry.get()
        cname = self.Name_Entry.get()
        cquantily = self.Quantily_Entry.get()
        cunit = self.Unit_Entry.get()
        cprice = self.Price_Entry.get()
        self.Add_Commodity = CommodityController(cid, cname, cquantily, cunit, cprice)

        if cid.isdigit() and cquantily.isdigit() and cprice.isdigit():
            if len(self.Add_Commodity.getCID()) < 3:
                messagebox.showerror('Error', 'ID must have 3 or more numbers')
            elif self.Add_Commodity.getCName() == '' or self.Add_Commodity.getCUnit() == '':
                messagebox.showerror('Error', 'Please enter the full information')
            elif self.checkID(self.Add_Commodity.getCID()) == False:
                messagebox.showerror('Error', 'This ID is available')
            else:
                # Add to file
                Write_File = ReadnWriteF.ReadnWrite_File_Commodity(self, 'a')
                Write_File.write(cid + " " + cname + " " + cquantily + ' ' + cunit + ' ' + cprice)
                Write_File.write('\n')
                Write_File.close()

                # Delete all the entry content
                self.SearchID_Entry.delete(0, 'end')
                self.ID_Entry.delete(0, 'end')
                self.Name_Entry.delete(0, 'end')
                self.Quantily_Entry.delete(0, 'end')
                self.Price_Entry.delete(0, 'end')
                self.Unit_Entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", 'ID, Quantily and Price are number')

def main3():
    root = Tk()
    Edit_Commodity(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=600, height=600)
    root.geometry("600x600")
    root.configure(bg='#88effc')
    root.mainloop()


if __name__ == "__main__":
    main3()
