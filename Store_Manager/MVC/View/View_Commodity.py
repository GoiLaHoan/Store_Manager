from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class View_Commodity(object):
    def show(self, tempList):
        for i, (ID, Name, Quantily, Unit, Price) in enumerate(tempList, start=1):
            self.listBox.insert("", "end", values=(ID, Name, Quantily, Unit, Price))

    def searchCom(self):
        f = open('./../../Data/Data_Commodity.txt', 'rt', encoding='utf-8')
        cid = self.cInfo1.get()

        if cid == '':
            messagebox.showerror('Lỗi', "Vui lòng nhập ID")
        else:
            found = False
            for i in self.listBox.get_children():
                self.listBox.delete(i)
            for line in f:
                file2 = []
                line = line.replace('(', '').replace(')', '').split()
                if (cid in line[0]):
                    found = True
                    file2.append(line)
                    self.show(file2)
            if found == False:
                messagebox.showerror('Lỗi', "Không tìm thấy sách có ID này")

    def update(self):
        f = open('./../../Data/Data_Commodity.txt', 'rt', encoding='utf-8')
        for i in self.listBox.get_children():
            self.listBox.delete(i)
        for line in f:
            file2 = []
            line = line.split()
            file2.append(line)
            self.show(file2)

        self.cInfo1.delete(0, 'end')
    def delete(self):
        cid = self.cInfo1.get()
        with open('./../../Data/Data_Commodity.txt', "r+") as f:
            if cid == '':
                messagebox.showerror('Lỗi', "Vui lòng nhập ID")
            else:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    a = i.split()
                    if a[0] != cid:
                        f.write(i)
                f.truncate()
        self.cInfo1.delete(0, END)
        self.update()



    def __init__(self, master):
        self.master = master

        # =============Title Search/Delete Commodity===========
        self.headingFrame1 = Frame(master, bg="#fff5b5", bd=4, )
        self.headingFrame1.place(relx=0.1, rely=0.05, relwidth=0.5, relheight=0.13)

        self.headingLabel = Label(self.headingFrame1, text="View Commodity", bg='#6b81ff', fg='black',
                                  font=('arial bold', 15))
        self.headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # =============Commodity ID===========
        self.labelFrame = Frame(master, bg='#6b81ff')
        self.labelFrame.place(relx=0.62, rely=0.065, relwidth=0.28, relheight=0.1)

        self.lb2 = Label(self.labelFrame, text="ID Commodity: ", bg='#6b81ff', fg='white')
        self.lb2.place(relx=0.05, rely=0.31)
        # global cInfo1
        self.cInfo1 = Entry(self.labelFrame)
        self.cInfo1.place(relx=0.4, rely=0.31, relwidth=0.50)

        f = open('./../../Data/Data_Commodity.txt', 'rt', encoding='utf-8')
        tempList = []
        for line in f:
            line = line.replace('(', '').replace(')', '').split()
            tempList.append(line)

        label = tk.Label(master, text="Commodity", font=("Arial", 30)).place(relx=0.3, rely=0.5)
        # create Treeview with 6 columns
        self.cols = ('ID', 'Name', 'Quantily', 'Unit', 'Price')
        self.listBox = ttk.Treeview(master, columns=self.cols, show='headings')
        # set column headings
        for col in self.cols:
            self.listBox.heading(col, text=col)
        self.listBox.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.55)
        self.show(tempList)


        # Update Button
        self.UpdateBtn = Button(master, text="Update", fg='Green', command=self.update)
        self.UpdateBtn.place(relx=0.44, rely=0.9, relwidth=0.1, relheight=0.08)


        # Delete Button
        self.DelBtn = Button(master, text="Delete", fg='#ffa200', command=self.delete)
        self.DelBtn.place(relx=0.56, rely=0.9, relwidth=0.1, relheight=0.08)

        # Search Button
        self.SeBtn = Button(master, text="Search", fg='#1900ff', command=self.searchCom)
        self.SeBtn.place(relx=0.68, rely=0.9, relwidth=0.1, relheight=0.08)

        # Quit Button
        self.quitBtn = Button(master, text="Quit", fg="Red", command=master.destroy)
        self.quitBtn.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.08)

def main3():
    root = Tk()
    View_Commodity(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=1280, height=720)
    root.geometry("1280x720")
    root.configure(bg='#88effc')
    root.mainloop()


if __name__ == "__main__":
    main3()