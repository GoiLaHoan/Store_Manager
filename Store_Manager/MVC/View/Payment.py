from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime



class Payment(object):
    total_cost = 0
    # listName = []
    # listQuantily = []
    # listPrice = []
    # listID = []
    def readData(self):
        self.listName = []
        self.listQuantily = []
        self.listPrice = []
        self.listID = []
        f = open('./../../Data/Data_Commodity.txt', 'rt', encoding='utf-8')
        for line in f:
            list1 = line.split()
            self.listID.append(list1[0])
            self.listName.append(list1[1] + ' (' + list1[3] + ')')
            self.listQuantily.append(list1[2])
            self.listPrice.append(list1[4])
    def __init__(self, master):

        self.master = master

        # ===========Tao Title Add Commodity ============
        self.headingFrame1 = Frame(master, bg="#ff66f5", bd=5)
        self.headingFrame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)

        self.headingLabel = Label(self.headingFrame1, text="Bill Commodity", bg='#fff5b5', fg='black',
                                  font=('Courier', 15))
        self.headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ===================product details====================
        # welcome=Label(master, text='Welcome to my store', font='arial 18 bold', fg='red')
        # welcome.place(relx=0.58, rely=0.83, relwidth=0.4, relheight=0.155)
        F1 = LabelFrame(master, text='Product Details', font='arial 18 bold', fg='red', bg='#88effc')
        F1.place(x=5, y=100, width=630, height=490)

        my_canvas = Canvas(F1, bg='#88effc')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(F1, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas, bg='#88effc')

        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

        itm1 = Label(second_frame, text="Items", font=('Helvetic', 18, 'bold', 'underline'), fg='black', bg='#88effc')
        itm1.grid(row=0, column=0, padx=20, pady=15)

        itm2 = Label(second_frame, text="Quantily of Items", font=('Helvetic', 18, 'bold', 'underline'), fg='black',
                     bg='#88effc')
        itm2.grid(row=0, column=1, padx=20, pady=15)

        itm3 = Label(second_frame, text="Price of Items", font=('Helvetic', 18, 'bold', 'underline'), fg='black',
                     bg='#88effc')
        itm3.grid(row=0, column=2, padx=20, pady=15)



        self.readData()
        self.my_lbNames, self.my_etQuas, self.my_lbPrices, self.my_etTotals, self.texttotals, self.textQuas = [], [], [], [], [], []
        for i in range(len(self.listName)):
            self.texttotal = IntVar()

            self.textQua = IntVar()
            self.lbName = Label(second_frame, text=self.listName[i], font='arial 15 bold', bg='#88effc',
                                fg='#004d99').grid(row=i + 1, column=0, pady=10, padx=10)
            self.etQua = Entry(second_frame, textvariable=self.textQua)
            self.etQua.grid(row=i + 1, column=1, pady=10, padx=10)
            self.lbPrice = Label(second_frame, text='$'+self.listPrice[i], font='arial 15 bold', bg='#88effc').grid(row=i + 1,column=2,pady=10,padx=10)
            self.my_lbNames.append(self.lbName)
            self.my_etQuas.append(self.etQua)
            self.my_lbPrices.append(self.lbPrice)
            self.my_etTotals.append(self.etQua)
            self.texttotals.append(self.texttotal)
            self.textQuas.append(self.textQua)


        F2 = Frame(master, relief=GROOVE, bd=10)
        F2.place(x=640, y=100, width=440, height=607)
        now = datetime.now()
        bill_title = Label(F2, text=f'Store_Python\n\nReceipt              {now.strftime("%d/%m/%Y %H:%M:%S")}', font=('Helvetic', 18, 'bold'), fg='black')
        bill_title.pack()
        scrol = Scrollbar(F2, orient=VERTICAL)
        scrol.pack(side=RIGHT, fill=Y)
        self.textarea = Text(F2, font='arial 15 bold', yscrollcommand=scrol.set)
        self.textarea.pack(fill=BOTH)
        scrol.config(command=self.textarea.yview())

        F3 = Frame(master, relief=GROOVE, bd=10)
        F3.place(x=5, y=600, width=630, height=110)

        bt1 = Button(F3, text='Print Bill', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5,
                     command=self.printbill)
        bt1.place(relx=0.01, rely=0.15, relwidth=0.2, relheight=0.7)

        bt2 = Button(F3, text='Receipt', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=self.receipt)
        bt2.place(relx=0.26, rely=0.15, relwidth=0.2, relheight=0.7)

        bt3 = Button(F3, text='Resert', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5,
                     command=self.resert)
        bt3.place(relx=0.53, rely=0.15, relwidth=0.2, relheight=0.7)

        bt4 = Button(F3, text='Exit', font='arial 15 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=master.destroy)
        bt4.place(relx=0.79, rely=0.15, relwidth=0.2, relheight=0.7)




    def printbill(self):
        self.total_cost = 0
        flag=True
        for i in range(len(self.listPrice)):
            if self.my_etQuas[i].get() == '':
                self.my_etQuas[i].delete(0, END)
                self.my_etQuas[i].insert(END, 0)
            if int(self.my_etQuas[i].get()) > int(self.listQuantily[i]):
                flag=False
                messagebox.showerror("Error", self.listName[i]+' in exceed the number of items, MAX: '+self.listQuantily[i])
                self.textQuas[i].set(self.listQuantily[i])
            else:
                self.my_etTotals[i] = int(self.my_etQuas[i].get()) * int(self.listPrice[i])
                self.texttotals[i].set(self.my_etTotals[i])

                self.total_cost+=self.my_etTotals[i]

        if flag:
            if self.total_cost != 0:
                self.textarea.delete(1.0, END)
                self.textarea.insert(END, '   Items\t\tNumber\t       Price\n\n')

                for i in range(len(self.listPrice)):
                    if int(self.my_etQuas[i].get()) > 0:
                        self.textarea.insert(END, self.listName[i] + '\t\t     ' + self.my_etQuas[i].get() + '\t       ' +
                                             self.listPrice[i] + '\n')
                self.textarea.insert(END, '--------------------------------------------------------\n')
                self.textarea.insert(END, f'Total_Cost: \t${self.total_cost}')
            else:
                messagebox.showerror("Error", 'You need to enter quantity')

    def resert(self):
        self.textarea.delete(0.0, END)
        for i in range(len(self.listPrice)):
            self.texttotals[i].set(0)
            self.textQuas[i].set(0)
        for i in range(len(self.listPrice)):
            self.my_etQuas[i].delete(0, END)
            self.my_etQuas[i].insert(END, 0)

            # self.my_etTotals[i].delete(0, END)
            # self.my_etTotals[i].insert(END, 5)
        self.total_cost = 0
        self.readData()

    def receipt(self):
        if self.total_cost == 0:
            messagebox.showerror("Error", "You need to click Print Bill")
        else:
            self.updateNum()
            self.resert
            messagebox.showinfo("Done", "Thank you for your purchase\n           See you later")
    def updateNum(self):
        with open('./../../Data/Data_Commodity.txt', 'r+', encoding='utf-8') as f:
            d = f.readlines()
            listE=[]
            f.seek(0)
            for w in d:
                line = w.split()
                listE.append(line)
            for i in range(len(d)):
                if self.listID[i] == listE[i][0]:
                    d[i] = d[i].replace(listE[i][2], str(int(listE[i][2])-int(self.my_etQuas[i].get())), 1)
                f.write(d[i])
            f.truncate()


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
