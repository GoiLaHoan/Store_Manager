from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF


class View_Commodity(object):
    def __init__(self, master):
        self.master = master

        '''
        Design Heading View
        '''
        self.Heading_View = Frame(master, bg="#fff5b5", bd=4, )
        self.Heading_View.place(relx=0.1, rely=0.05, relwidth=0.5, relheight=0.13)

        self.View_Label = Label(self.Heading_View, text="View Commodity", bg='#6b81ff', fg='black',
                                  font=('arial bold', 15))
        self.View_Label.place(relx=0, rely=0, relwidth=1, relheight=1)

        '''
        Design ID Commodity
        '''
        self.ID_Commodity_Frame = Frame(master, bg='#6b81ff')
        self.ID_Commodity_Frame.place(relx=0.62, rely=0.065, relwidth=0.28, relheight=0.1)

        self.ID_Commodity_Label = Label(self.ID_Commodity_Frame, text="ID Commodity: ", bg='#6b81ff', fg='white')
        self.ID_Commodity_Label.place(relx=0.05, rely=0.31)

        self.ID_Commodity_Entry = Entry(self.ID_Commodity_Frame)
        self.ID_Commodity_Entry.place(relx=0.4, rely=0.31, relwidth=0.50)


        '''
        Create TreeView
        '''
        #Create list data tempList
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        tempList = []
        for line in f:
            if len(line) > 0 :
                line = line.split()
                tempList.append(line)

        # Create Treeview with 6 columns
        self.cols = ('ID', 'Name', 'Quantily', 'Unit', 'Price')
        self.listBox = ttk.Treeview(master, columns=self.cols, show='headings')
        # set column headings
        for col in self.cols:
            self.listBox.heading(col, text=col)
        self.listBox.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.55)
        self.show(tempList)

        '''
        Design Button
        '''
        # Update Button
        self.UpdateBtn = Button(master, text="Update", fg='Green', command=self.update)
        self.UpdateBtn.place(relx=0.44, rely=0.9, relwidth=0.1, relheight=0.08)

        # Delete Button
        self.DelBtn = Button(master, text="Delete", fg='#ffa200', command=self.delete)
        self.DelBtn.place(relx=0.56, rely=0.9, relwidth=0.1, relheight=0.08)

        # Search Button
        self.SearchBtn = Button(master, text="Search", fg='#1900ff', command=self.search)
        self.SearchBtn.place(relx=0.68, rely=0.9, relwidth=0.1, relheight=0.08)

        # Quit Button
        self.QuitBtn = Button(master, text="Quit", fg="Red", command=master.destroy)
        self.QuitBtn.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.08)



    def show(self, tempList):
        if len(tempList) >0 :
            for i, (ID, Name, Quantily, Unit, Price) in enumerate(tempList, start=1):
                self.listBox.insert("", "end", values=(ID, Name, Quantily, Unit, Price))

    def search(self):
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        self.cid = self.ID_Commodity_Entry.get()
        if self.cid == '':
            messagebox.showerror('Error', "Please enter ID")
        else:
            found = False
            for i in self.listBox.get_children():
                self.listBox.delete(i)
            for line in f:
                file2 = []
                line = line.split()
                if (self.cid in line[0]):
                    found = True
                    file2.append(line)
                    self.show(file2)
            if found == False:
                messagebox.showerror('Error', "This ID was not found")
        f.close()

    def update(self):
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        for i in self.listBox.get_children():
            self.listBox.delete(i)
        for line in f:
            file2 = []
            line = line.split()
            file2.append(line)
            self.show(file2)
        f.close()
        self.ID_Commodity_Entry.delete(0, 'end')

    def delete(self):
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'r+')
        self.cid = self.ID_Commodity_Entry.get()
        if self.cid == '':
            messagebox.showerror('Error', "Please enter ID")
        else:
            d = f.readlines()
            f.seek(0)
            for i in d:
                a = i.split()
                if a[0] != self.cid:
                    f.write(i)
            f.truncate()
        f.close()
        self.ID_Commodity_Entry.delete(0, END)
        self.update()


def main1():
    root = Tk()
    View_Commodity(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=1280, height=720)
    root.geometry("1280x720")
    root.configure(bg='#88effc')
    root.mainloop()


if __name__ == "__main__":
    main1()
