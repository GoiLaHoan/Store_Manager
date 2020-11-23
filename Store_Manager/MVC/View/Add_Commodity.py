from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MVC.Controller.Commodity_Controller import CommodityController
from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF


class Add_Commodity(object):

    def __init__(self, master):
        self.master = master

        '''
        Create Heading Frame Add Commodity
        '''
        self.headingFrameAdd = Frame(master, bg="#ff66f5", bd=5)
        self.headingFrameAdd.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.21)

        self.headingLb = Label(self.headingFrameAdd, text="Add Commodity", bg='#fff5b5', fg='black',
                               font=('Courier', 15))
        self.headingLb.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ===========================================

        self.cid = IntVar()
        self.name = StringVar()
        self.quantily = IntVar()
        self.price = IntVar()
        # ===========================================

        '''
        Design FrameAdd
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

        self.Unit_Entry = ttk.Combobox(self.labelFrame)
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
        # Submit Button
        self.SubmitBtn = Button(master, text="SUBMIT", fg="Green", command=self.submit)
        self.SubmitBtn.place(relx=0.28, rely=0.86, relwidth=0.18, relheight=0.08)

        # Quit Button
        self.QuitBtn = Button(master, text="Quit", fg="Red", command=master.destroy)
        self.QuitBtn.place(relx=0.53, rely=0.86, relwidth=0.18, relheight=0.08)

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
                self.ID_Entry.delete(0, 'end')
                self.Name_Entry.delete(0, 'end')
                self.Quantily_Entry.delete(0, 'end')
                self.Price_Entry.delete(0, 'end')
                self.Unit_Entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", 'ID, Quantily and Price are number')


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
