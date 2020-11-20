from tkinter import *
from tkinter import ttk

class Payment(object):

    def __init__(self, master):
        self.master = master





        textetQua = IntVar()
        total=DoubleVar()
        textetQua.set(55)

        # self.my_entries = []
        # for x in range(5):
        #     my_entry = Entry(master)
        #     my_entry.grid(row=0, column=x, pady=20, padx=5)
        #     self.my_entries.append(my_entry)

        self.my_etQuas = []
        for i in range(6):
            self.etQua = Entry(master)
            self.etQua.grid(row=i+1, column=1, pady=10, padx=10)
            self.my_etQuas.append(self.etQua)


        F2=Frame(master, relief=GROOVE, bd=10)
        F2.place(x=820,y=100,width=440,height=490)
        bill_title=Label(F2, text='Receipt', font='arial 15 bold', bd =7,relief=GROOVE).pack(fill=X)
        scrol=Scrollbar(F2,orient=VERTICAL)
        scrol.pack(side=RIGHT,fill=Y)
        textarea=Text(F2,font='arial 15 bold', yscrollcommand=scrol.set)
        textarea.pack(fill=BOTH)
        scrol.config(command=textarea.yview())


        bt1=Button(master,text='Total',font='arial 20 bold',bg='yellow',fg='crimson',padx=5,pady=5, command=self.total)
        bt1.place(relx=0.5, rely=0.15, relwidth=0.15, relheight=0.7)

    def total(self):
        et_listQ = ''
        for etQ in self.my_etQuas:
            print(etQ.get())
            et_listQ = et_listQ + str(etQ.get()) + '\n'
            # print(et_listQ)



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