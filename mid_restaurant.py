from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import time


class Sea(Tk):
    def __init__(self):
        super().__init__()

        g = StringVar()
        g2 = StringVar()
        self.title("Main") 
        self.maxsize(1900,618)
        self.minsize(1900,618)
        w = 1900
        h = 618
        ws = self.winfo_screenwidth() 
        hs = self.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas = Canvas(width=1900, height=618, bg='black')
        self.canvas.pack()
        self.photo = PhotoImage(file="bgver3.png")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.iconbitmap(r'icon.ico')
        l1=Label(self,text="Main",font=("Algerian",20,'bold'),bg="#928076").place(x=400,y=20)
        l = Label(self, text="Order Cancel", font=("Arial", 15, 'bold'),bg="#928076").place(x=60, y=96)
        l11 = Label(self, text="Order make", font=("Arial", 15, 'bold'),bg="#928076").place(x=60, y=148)

        menu_make = []
        menu_list = []

        def white_update():
            with open("menu.txt", "w", encoding="utf8") as f:
                for m in menu_list:
                    f.write(str(m) )
            with open("menu_make.txt", "w", encoding="utf8") as f:
                for m in menu_make:
                    f.write(str(m) )
            

        def up_load_data_make():
            f = open("menu_make.txt")
            for row in f:
                menu_make.append(row)
            f.close()

           
        def up_load_data_list():
            f = open("menu.txt")
            for row in f:
                menu_list.append(row)
            f.close()


        def to_make():
            if (len(g2.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            else:
                order_to_make = g2.get()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print(order_to_make)
                print(type(order_to_make))
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
                for i in range(0,len(menu_list)):
                    print(menu_list[i])
                    if (menu_list[i]==order_to_make):
                        print("out make")
                        menu_make.append(menu_list[i])
                        menu_list.pop(i)
                        break
                white_update()
                reopen()

        def to_cancel():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            else:
                order_to_cancel = g.get()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print(order_to_cancel )
                print(type(order_to_cancel ))
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
                for i in range(0,len(menu_list)):
                    print(menu_list[i])
                    if (menu_list[i]==order_to_cancel):
                        print("out")
                        menu_list.pop(i)
                        break
                # menu_list.pop(0)
                white_update()
                reopen()

        up_load_data_make()
        up_load_data_list()


        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=18,columns=('Food Name', 'Type', 'Amount','Price','Time'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='ID', anchor='center')
        self.listTree.column("#0", width=20*3, anchor='center')
        self.listTree.heading("Food Name", text='Food Name')
        self.listTree.column("Food Name", width=20*10, anchor='center')
        self.listTree.heading("Type", text='Type')
        self.listTree.column("Type", width=20*7, anchor='center')
        self.listTree.heading("Amount", text='Amount')
        self.listTree.column("Amount", width=20*6, anchor='center')
        self.listTree.heading("Price", text='Price')
        self.listTree.column("Price", width=20*7, anchor='center')
        self.listTree.heading("Time", text='Time')
        self.listTree.column("Time", width=20*10, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=10, y=200)
        self.vsb.place(x=870,y=200,height=400)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))
        self.listTree.delete(*self.listTree.get_children())

        # data list and insert 
        for x in range(0,len(menu_list)):
            split_word = menu_list[x].split(",")
            print(split_word)
            word_in= ["","","","","","",""]
            for i in range(0,len(split_word)):
                for w in split_word[i]:
                    if(w == "," or w == " " or w == "'"  or w == "]" or w == "["):  
                        pass
                    else:
                        word_in[i] += str(w)
            self.listTree.insert("", 'end', text=word_in[0], values=(word_in[1], word_in[2], word_in[3], word_in[4],word_in[5]))

        self.listTree = ttk.Treeview(self, height=18,columns=('Food Name', 'Type', 'Amount','Price','Pay','Time'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='ID', anchor='center')
        self.listTree.column("#0", width=20*3, anchor='center')
        self.listTree.heading("Food Name", text='Food Name')
        self.listTree.column("Food Name", width=20*10, anchor='center')
        self.listTree.heading("Type", text='Type')
        self.listTree.column("Type", width=20*7, anchor='center')
        self.listTree.heading("Amount", text='Amount')
        self.listTree.column("Amount", width=20*6, anchor='center')
        self.listTree.heading("Price", text='Price')
        self.listTree.column("Price", width=20*7, anchor='center')
        self.listTree.heading("Pay", text='Pay')
        self.listTree.column("Pay", width=20*5, anchor='center')
        self.listTree.heading("Time", text='Time')
        self.listTree.column("Time", width=20*10, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=890, y=200)
        self.vsb.place(x=990+862,y=200,height=400)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        # data list_make and insert 
        for x in range(0,len(menu_make)):
            split_word = menu_make[x].split(",")
            word_in= ["","","","","","",""]
            for i in range(0,len(split_word)):
                for w in split_word[i]:
                    if(w == "," or w == " " or w == "'"  or w == "]" or w == "["):  
                        pass
                    else:
                        word_in[i] += str(w)
            self.listTree.insert("", 'end', text=word_in[0], values=(word_in[1], word_in[2], word_in[3], word_in[4],word_in[6],word_in[5]))
            
        def reopen():
            self.destroy()
            Sea().mainloop()
        

        def wirte_final_today():
            x= time.asctime(time.localtime(time.time()))
            x = x.split(" ")
            
            name = x[2]+"_"+x[1]+"_"+x[4]+".txt"
            print(name)
            with open(name, "a", encoding="utf8") as f:
                for m in menu_make:
                    f.write(str(m) )
            
            with open("menu_make_ALL.txt", "a", encoding="utf8") as f:
                for m in menu_make:
                    f.write(str(m) )

            menu_make.clear()
            white_update()
            reopen()
            
        c=ttk.Combobox(self,textvariable=g,values=menu_list,width=80,state="readonly").place(x =200, y = 106)
        c2=ttk.Combobox(self,textvariable=g2,values=menu_list,width=80,state="readonly").place(x =200, y = 157)



        B1=Button(self,text="GO",width=15,font=("Arial",10,'bold'),command=to_make).place(x=720,y=150)
        B2=Button(self,text="Export",width=15,font=("Arial",10,'bold'),command=wirte_final_today).place(x=1740,y=150)
        B3=Button(self,text="CANCEL",width=15,font=("Arial",10,'bold'),command=to_cancel).place(x=720,y=100)
        # def motion(event):
        #     x, y = event.x, event.y
        #     print('{}, {}'.format(x, y))

        # self.bind('<Motion>', motion)
        
            
Sea().mainloop()