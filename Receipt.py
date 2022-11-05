from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os.path


class Sea(Tk):
    def __init__(self):
        super().__init__()

        d = StringVar()
        self.title("Receipt")
        self.maxsize(1366,768)
        self.minsize(1366,768)
        w = 1366
        h = 768
        ws = self.winfo_screenwidth() 
        hs = self.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.canvas = Canvas(width=1366, height=768, bg='black')
        self.canvas.pack()
        self.photo = PhotoImage(file="bg.png")
       
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW) 
        
        self.iconbitmap(r'icon.ico')
        l1=Label(self,text="Serach_id",font=("Algerian",20,'bold'),bg="#8DA574").place(x=1100,y=100)
        l5 = Label(self,text="YOUR ORDER",bg="#9db1f2",font=("Cooper Black",22)).place(x=600, y=50)
        self.canvas.create_rectangle(400, 150, 1000, 700,fill="#d3ede6",outline="white",width=6)
        l6 = Label(self, text="Total : "+str(0),bg="#f2da9d",width=12,font=("Cooper Black",22)).place(x=1050, y=650)
        self.canvas.create_text(700,180,text="Items\tSize\tQty\tPrice",font=("cooper black",18))
        self.canvas.create_text(700,200,text="_______________________________________",font=("cooper black",18))
        menu_make = []
        menu_make_temp = []



        def up_load_data_make(namefile):
            f = open(namefile)
            for row in f:
                menu_make.append(row)
            f.close()
        

        def insert(id):
            have_id = False
            sum_price = 0
            ordertlist = []
            status = False
            for x in range(0,len(menu_make)):
                ordertlist_temp=[]
                split_word = menu_make[x].split(",")
                word_in= ["","","","","","",""]
                for i in range(0,len(split_word)):
                    for w in split_word[i]:
                        if(w == "," or w == " " or w == "'"  or w == "]" or w == "["):  
                            pass
                        else:
                            word_in[i] += str(w)
                print(word_in)
                if(word_in[0]==str(id)):
                    if(word_in[6][0]+word_in[6][1] == "No"):
                        status = False
                    else:
                        status = True
                    have_id = True
                    ordertlist_temp.append(word_in[1])
                    ordertlist_temp.append(word_in[2])
                    ordertlist_temp.append(word_in[3])
                    ordertlist_temp.append(word_in[4])
                    sum_price+=int(word_in[4])
                    ordertlist.append(ordertlist_temp)

            print(sum_price)
            if(have_id == False):
                messagebox.showinfo('Error', 'No information available for this id')

            self.canvas.create_rectangle(400, 150, 1000, 700,fill="#d3ede6",outline="white",width=6)
            self.canvas.create_text(700,180,text="Items\tSize\tQty\tPrice",font=("cooper black",18))
            self.canvas.create_text(700,200,text="_______________________________________",font=("cooper black",18))
            y=200
            j=0
            for i in ordertlist:
                print(i)
                y+=30
                s=i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+str(i[3])
                self.canvas.create_text(700,y,text=s,font=("default",16))
                j+=1
            l6 = Label(self, text="Total : "+str(sum_price),bg="#f2da9d",width=12,font=("Cooper Black",22)).place(x=1050, y=650)

            def Pay():
 
                if(status == False):
                    messagebox.showinfo('', 'successful payment')
                    #for menu_make
                    for k in range(0,len(menu_make_temp)):
                        menu_make_temp.pop()

                    for x in range(0,len(menu_make)):
                        split_word = menu_make[x].split(",")
                        word_in= ["","","","","","",""]
                        for i in range(0,len(split_word)):
                            for w in split_word[i]:
                                if(w == "," or w == " " or w == "'"  or w == "]" or w == "["):  
                                    pass
                                else:
                                    word_in[i] += str(w)
                        print("---")
                        if(word_in[0]==str(id)):
                                word_in[6] = "Yes"
                        elif(word_in[6][0]+word_in[6][1]=="No"):
                            word_in[6] = "No"
                        elif(word_in[6][0]+word_in[6][1]+word_in[6][2]=="Yes"):
                            word_in[6] = "Yes"
                        print(word_in)
                        menu_make_temp.append(word_in)
                    print("All")
                    print(menu_make_temp)
                    with open("menu_make.txt", "w", encoding="utf8") as f:
                        for m in menu_make_temp:
                            f.write(str(m) + "\n")
                    

                elif(status == True):
                    messagebox.showinfo('', 'This id has already paid')

            b2=Button(self,text="Pay",command=Pay,bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold')).place(x=1150,y=700)

        def ge():
            if (len(d.get())) == 0:
                messagebox.showinfo('Error', 'Enter the id')
            else:
                try:


                    file_exists = os.path.exists("menu_make.txt")
                    if(file_exists==True):
                        for kk in range(0,len(menu_make)):
                            menu_make.pop()
                        up_load_data_make("menu_make.txt")  
                        insert(d.get())
                    else:
                        messagebox.showinfo('Error', 'Something goes wrong')
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        b=Button(self,text="Find",width=15,font=("Arial",10,'bold'),command=ge).place(x=1050,y=200)
        en = Entry(self,textvariable=d,width=43).place(x=1050,y=250)

        

Sea().mainloop()