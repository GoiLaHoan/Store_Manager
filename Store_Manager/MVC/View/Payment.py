from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from MVC.Controller.ReadnWriteF_Commodity import ReadnWriteF
from MVC.Controller.Commodity_Controller import CommodityController


class Payment(object):
    total_cost = 0

    def __init__(self, master):

        self.master = master

        '''
        Create Heading Frame Payment
        '''
        self.Heading_Frame = Frame(master, bg="#ff66f5", bd=5)
        self.Heading_Frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)

        self.Heading_Label = Label(self.Heading_Frame, text="Bill Commodity", bg='#fff5b5', fg='black',
                                  font=('Courier', 15))
        self.Heading_Label.place(relx=0, rely=0, relwidth=1, relheight=1)

        '''
        Create Product Details
        '''
        #Create Label Frame Product Details
        F1 = LabelFrame(master, text='Product Details', font='arial 18 bold', fg='red', bg='#88effc')
        F1.place(x=5, y=100, width=630, height=490)

        #Create ScrollBar
        my_canvas = Canvas(F1, bg='#88effc')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(F1, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas, bg='#88effc')

        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

        # Create Label Item, Quantily, Price
        Item_Label = Label(second_frame, text="Items", font=('Helvetic', 18, 'bold', 'underline'), fg='black', bg='#88effc')
        Item_Label.grid(row=0, column=0, padx=20, pady=15)

        Quantily_Label = Label(second_frame, text="Quantily of Items", font=('Helvetic', 18, 'bold', 'underline'), fg='black',
                     bg='#88effc')
        Quantily_Label.grid(row=0, column=1, padx=20, pady=15)

        Price_Label = Label(second_frame, text="Price of Items", font=('Helvetic', 18, 'bold', 'underline'), fg='black',
                     bg='#88effc')
        Price_Label.grid(row=0, column=2, padx=20, pady=15)

        #Create lists in the data
        self.readData()

        # Create lists name of data
        self.ListName_Label, self.ListQuantily_Entry, self.ListPrice_Label, self.ListTotal_Entry = [], [], [], []

        # Create lists textvariable
        self.textTotals, self.textQuantily = [], []


        for i in range(len(self.listName)):

            self.texttotal = IntVar()
            self.textQua = IntVar()

            self.Name_Label = Label(second_frame, text=self.listName[i], font='arial 15 bold', bg='#88effc', fg='#004d99')
            self.Name_Label.grid(row=i + 1, column=0, pady=10, padx=10)

            self.Quantily_Entry = Entry(second_frame, textvariable=self.textQua)
            self.Quantily_Entry.grid(row=i + 1, column=1, pady=10, padx=10)

            self.Price_Label = Label(second_frame, text='$'+self.listPrice[i], font='arial 15 bold', bg='#88effc')
            self.Price_Label.grid(row=i + 1,column=2,pady=10,padx=10)

            #Add data to the list
            self.ListName_Label.append(self.Name_Label)
            self.ListQuantily_Entry.append(self.Quantily_Entry)
            self.ListPrice_Label.append(self.Price_Label)
            self.ListTotal_Entry.append(self.Quantily_Entry)
            self.textTotals.append(self.texttotal)
            self.textQuantily.append(self.textQua)

        '''
        Design Bill
        '''
        F2 = Frame(master, relief=GROOVE, bd=10)
        F2.place(x=640, y=100, width=440, height=607)

        now = datetime.now()
        bill_title = Label(F2, text=f'Store_Python\n\nReceipt\t\t{now.strftime("%d/%m/%Y %H:%M:%S")}', font=('Helvetic', 16, 'bold'), fg='black')
        bill_title.pack()

        scrol = Scrollbar(F2, orient=VERTICAL)
        scrol.pack(side=RIGHT, fill=Y)

        self.textarea = Text(F2, font='arial 15 bold', yscrollcommand=scrol.set)
        self.textarea.pack(fill=BOTH)
        scrol.config(command=self.textarea.yview())

        '''
        Design Button
        '''
        F3 = Frame(master, relief=GROOVE, bd=10)
        F3.place(x=5, y=600, width=630, height=110)

        #Print
        printBtn = Button(F3, text='Print Bill', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5,command=self.printbill)
        printBtn.place(relx=0.01, rely=0.15, relwidth=0.2, relheight=0.7)

        #Receipt
        receiptBtn = Button(F3, text='Receipt', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=self.receipt)
        receiptBtn.place(relx=0.26, rely=0.15, relwidth=0.2, relheight=0.7)

        #Resert
        resertBtn = Button(F3, text='Resert', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5,command=self.resert)
        resertBtn.place(relx=0.53, rely=0.15, relwidth=0.2, relheight=0.7)

        #Exit
        exitBtn = Button(F3, text='Exit', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=master.destroy)
        exitBtn.place(relx=0.79, rely=0.15, relwidth=0.2, relheight=0.7)


    def readData(self):
        self.listName = []
        self.listQuantily = []
        self.listPrice = []
        self.listID = []
        self.listUnit = []
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'rt')
        for line in f:
            listData = line.split()
            self.listID.append(listData[0])
            self.listName.append(listData[1])
            self.listQuantily.append(listData[2])
            self.listUnit.append(listData[3])
            self.listPrice.append(listData[4])
    def outputData(self):
        f = ReadnWriteF.ReadnWrite_File_Sales(self, 'a')
        now = datetime.now()
        f.write(str(now.strftime("%d/%m/%Y %H:%M:%S")) + '\n\n')
        for i in range(len(self.listName)):
            if int(self.ListQuantily_Entry[i].get())>0:
                line=self.listID[i]+' '+self.listName[i]+' '+self.ListQuantily_Entry[i].get()+' '+self.listUnit[i]+' '+self.listPrice[i]
                f.write(line+'\n')
        f.write('-'*30+'\n')
        f.close()

    def printbill(self):
        self.total_cost = 0

        flag=True
        for i in range(len(self.listPrice)):
            if self.ListQuantily_Entry[i].get() == '':
                self.ListQuantily_Entry[i].delete(0, END)
                self.ListQuantily_Entry[i].insert(END, 0)
            if int(self.ListQuantily_Entry[i].get()) > int(self.listQuantily[i]):
                flag=False
                messagebox.showerror("Error", self.listName[i]+' in exceed the number of items, MAX: '+self.listQuantily[i])
                self.textQuantily[i].set(self.listQuantily[i])
            else:
                self.ListTotal_Entry[i] = int(self.ListQuantily_Entry[i].get()) * int(self.listPrice[i])
                self.textTotals[i].set(self.ListTotal_Entry[i])
                self.total_cost+=self.ListTotal_Entry[i]

        if flag:
            if self.total_cost != 0:
                self.textarea.delete(1.0, END)
                self.textarea.insert(END, 'Items\t\tNumber\t       Price\n\n')

                for i in range(len(self.listPrice)):
                    if int(self.ListQuantily_Entry[i].get()) > 0:
                        self.textarea.insert(END, self.listName[i] + '\t\t     ' + self.ListQuantily_Entry[i].get() + '\t       ' + self.listPrice[i] + '\n')
                self.textarea.insert(END, '--------------------------------------------------------\n')
                self.textarea.insert(END, f'Total_Cost: \t${self.total_cost}')
            else:
                messagebox.showerror("Error", 'You need to enter quantity')


    def resert(self):
        self.textarea.delete(0.0, END)
        for i in range(len(self.listPrice)):
            self.textTotals[i].set(0)
            self.textQuantily[i].set(0)
        for i in range(len(self.listPrice)):
            self.ListQuantily_Entry[i].delete(0, END)
            self.ListQuantily_Entry[i].insert(END, 0)

        self.total_cost = 0
        self.readData()


    def receipt(self):
        if self.total_cost == 0:
            messagebox.showerror("Error", "You need to click Print Bill")
        else:
            self.updateNum()
            self.outputData()
            self.resert()
            messagebox.showinfo("Done", "Thank you for your purchase\n           See you later")


    def updateNum(self):
        f = ReadnWriteF.ReadnWrite_File_Commodity(self, 'r+')
        d = f.readlines()
        listE=[]
        f.seek(0)
        for w in d:
            line = w.split()
            listE.append(line)
        for i in range(len(d)):
            if self.listID[i] == listE[i][0]:
                listE[i][2] = str(listE[i][2]).replace(listE[i][2],str(int(listE[i][2])-int(self.ListQuantily_Entry[i].get())))
            f.write(str(listE[i]).strip('[]').replace(',', '').replace('\'', '') + '\n')
        f.truncate()
        f.close()


def main4():
    root = Tk()
    Payment(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=1100, height=720)
    root.maxsize(width=1100, height=720)
    root.resizable(False, False)
    root.geometry("1100x720")
    root.mainloop()


if __name__ == "__main__":
    main4()
