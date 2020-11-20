from tkinter import *
class name():

    def __init__(self):
        root = Tk()
        com2 = Label(root, text="Name      : ", bg='#99ccff', fg='#004d99')
        com2.place(relx=0.05, rely=0.35, relheight=0.1)
        btnt = Button(root, text='Enter', command=self.total())

        btnt.place(relx=0.4, rely=0.5, relwidth=0.72, relheight=0.1)

        self.my_entries = []
        for x in range(5):
            my_entry = Entry(root)
            my_entry.grid(row=0, column=x, pady=20, padx=5)
            self.my_entries.append(my_entry)
        print(self.my_entries)
        root.mainloop()
    def total(self):
        et_listQ = ''
        for etQ in self.my_entries:
            print(etQ.get())
            et_listQ = et_listQ +str(etQ.get())+'\n'
            # print(et_listQ)
name()