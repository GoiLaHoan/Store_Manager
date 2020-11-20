from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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
        F1 = LabelFrame(master, text='Product Details', font='arial 18 bold', fg='red', bg='#88effc')
        F1.place(x=5, y=100, width=800, height=490)

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

        itm4 = Label(second_frame, text="Total money", font=('Helvetic', 18, 'bold', 'underline'), fg='black',
                     bg='#88effc')
        itm4.grid(row=0, column=3, padx=20, pady=15)


        self.readData()
        self.my_lbNames, self.my_etQuas, self.my_lbPrices, self.my_etTotals, self.texttotals, self.textQuas = [], [], [], [], [], []
        for i in range(len(self.listName)):
            self.texttotal = IntVar()
            self.textQua=IntVar()
            self.lbName = Label(second_frame, text=self.listName[i], font='arial 15 bold', bg='#88effc',
                                fg='#004d99').grid(row=i + 1, column=0, pady=10, padx=10)
            self.etQua = Entry(second_frame, textvariable=self.textQua)
            self.etQua.grid(row=i + 1, column=1, pady=10, padx=10)
            self.lbPrice = Label(second_frame, text='$'+self.listPrice[i], font='arial 10', bg='#88effc').grid(row=i + 1,column=2,pady=10,padx=10)
            self.etTotal = Entry(second_frame, textvariable=self.texttotal)
            self.etTotal.grid(row=i + 1, column=3, pady=10, padx=10)
            self.my_lbNames.append(self.lbName)
            self.my_etQuas.append(self.etQua)
            self.my_lbPrices.append(self.lbPrice)
            self.my_etTotals.append(self.etTotal)
            self.texttotals.append(self.texttotal)
            self.textQuas.append(self.textQua)

        F2 = Frame(master, relief=GROOVE, bd=10)
        F2.place(x=820, y=100, width=440, height=490)
        bill_title = Label(F2, text='Receipt', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scrol = Scrollbar(F2, orient=VERTICAL)
        scrol.pack(side=RIGHT, fill=Y)
        self.textarea = Text(F2, font='arial 15 bold', yscrollcommand=scrol.set)
        self.textarea.pack(fill=BOTH)
        scrol.config(command=self.textarea.yview())

        F3 = Frame(master, relief=GROOVE, bd=10)
        F3.place(x=5, y=600, width=800, height=110)

        bt1 = Button(F3, text='Total', font='arial 20 bold', bg='yellow', fg='crimson', padx=5, pady=5,
                     command=self.total)
        bt1.place(relx=0.01, rely=0.15, relwidth=0.15, relheight=0.7)

        bt2 = Button(F3, text='Receipt', font='arial 20 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=self.receipt)
        bt2.place(relx=0.26, rely=0.15, relwidth=0.15, relheight=0.7)

        bt3 = Button(F3, text='Reset', font='arial 20 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=self.resert)
        bt3.place(relx=0.53, rely=0.15, relwidth=0.15, relheight=0.7)

        bt4 = Button(F3, text='Exit', font='arial 20 bold', bg='yellow', fg='crimson', padx=5, pady=5, command=master.destroy)
        bt4.place(relx=0.81, rely=0.15, relwidth=0.15, relheight=0.7)




    def total(self):
        for i in range(len(self.listPrice)):
            if int(self.my_etQuas[i].get()) > int(self.listQuantily[i]):
                messagebox.showerror("Error", self.listName[i]+' in exceed the number of items')
                self.textQuas[i].set(self.listQuantily[i])
            else:
                self.my_etTotals[i] = int(self.my_etQuas[i].get()) * int(self.listPrice[i])
                self.texttotals[i].set(self.my_etTotals[i])
                self.total_cost+=self.my_etTotals[i]

    def resert(self):
        self.textarea.delete(0.0, END)
        for i in range(len(self.listPrice)):
            self.texttotals[i].set(0)
            self.textQuas[i].set(0)
        self.total_cost = 0

        self.readData()
    def receipt(self):
        if self.total_cost == 0:
            messagebox.showerror("Error", "You need to total before printing the receipt")
        else:
            self.textarea.delete(1.0, END)
            self.textarea.insert(END,'   Items\t\tNumber\t       Price\n\n')

            for i in range(len(self.listPrice)):
                if int(self.my_etQuas[i].get())>0:
                    self.textarea.insert(END, self.listName[i]+'\t\t     '+self.my_etQuas[i].get()+'\t       '+self.listPrice[i]+'\n' )
            self.textarea.insert(END, '--------------------------------------------------------\n')
            self.textarea.insert(END, f'Total_Cost: \t${self.total_cost}')
            self.updateNum()

    def updateNum(self):
        with open('./../../Data/Data_Commodity.txt', 'r+', encoding='utf-8') as f:
            d = f.readlines()
            listE=[]
            f.seek(0)
            for w in d:
                line = w.split()
                listE.append(line)

            for i in range(len(d)):
                for j in range(len(self.listPrice)):
                    if self.listID[j] == listE[i][0]:
                        d[i] = d[i].replace(listE[i][2], str(int(listE[i][2])-int(self.my_etQuas[j].get())))
                f.write(d[i])
            f.truncate()
            messagebox.showinfo("Noti", "Done")
def main4():
    root = Tk()
    Payment(root)
    root.title("Mini Shop")
    root.iconbitmap('shop.ico')
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.resizable(False, False)
    root.geometry("1280x720")
    root.mainloop()


if __name__ == "__main__":
    main4()
