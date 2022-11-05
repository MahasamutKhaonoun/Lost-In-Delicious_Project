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
        m = StringVar()
        y = StringVar()
        sum_price = 0
        No_pay = 0
        self.title("Summary")
        self.maxsize(1000,600)
        self.minsize(1000,600)
        w = 1000
        h = 600
        ws = self.winfo_screenwidth() 
        hs = self.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y1 = (hs/2) - (h/2) -25
        self.geometry('%dx%d+%d+%d' % (w, h, x, y1))
        
        self.canvas = Canvas(width=1000, height=600, bg='black')
        self.canvas.pack()
        self.photo = PhotoImage(file="bg.png")
        self.canvas.create_image(-20, -20, image=self.photo, anchor=NW)

        self.iconbitmap(r'icon.ico')
        l1=Label(self,text="Summary",font=("Arial",20,'bold'),bg="#928076",fg="white").place(x=290,y=20)
        l2 = Label(self, text="Month" , font=("Arial", 15, 'bold'),bg="#928076",fg="white").place(x=100, y=96)
        l3 = Label(self, text="year" , font=("Arial", 15, 'bold'),bg="#928076",fg="white").place(x=100, y=200)
        l4 = Label(self, text="day", font=("Arial", 15, 'bold'),bg="#928076",fg="white").place(x=100, y=150)
        l5 = Label(self, text="Paid : "+str(sum_price),bg="#f2da9d",width=20,font=("Cooper Black",12)).place(x=20, y=550)
        l6 = Label(self, text="No paid : "+str(No_pay),bg="#f2da9d",width=20,font=("Cooper Black",12)).place(x=20, y=520)
        menu_make = []
        Qrder_quantity={"DeluxeVeggie":int(0),"VegVaganza":int(0),"5Pepper":int(0),"Margherita":int(0),"FishHeadSoup":int(0),"SpinachWith3Eggs":int(0),"ClearSoupwithBeanCurd":int(0),"SpicyCatfish":int(0),"FieryPorkRibsBroth":int(0),
    "SpicyMushroomSoup":int(0),"ShrimpCakes":int(0),"FriedFish-pasteBalls":int(0),"FriedChickenwithFishSauce":int(0),"FriedSunDriedPork":int(0),
    "FriedChineseChives":int(0),"FriedDumplings":int(0),"StirFriedPorkLiverwithChineseChives":int(0),"StirFriedPorkwithShrimpPaste":int(0),"StirFriedPorkLiverwithChili":int(0),"StirFriedB.EggwithBasil":int(0),
    "SpicyStirFriedCatfish":int(0),"FriedTofuandPrawnSauce":int(0),"SpicySalmonSalad":int(0),"SaltedEggSpicySalad":int(0),"SpicyCockleSalad":int(0),"ShrimpSalad":int(0),"BlueCrabSalad":int(0),"SpicySeafoodSalad":int(0),
    "PorkSatay":int(0),"StickyRice":int(0),"CookedRice":int(0),"LargeCookedRice":int(0),"GreenCurry":int(0),"PanangCurry":int(0),"KaengTaePo":int(0),"FishOrgansSourSoup":int(0),"KaengOom":int(0),"MassamanCurry":int(0)}

        def up_load_data_make(namefile):
            print("1")
            print(menu_make)
            for i in range(0,len(menu_make)):
                menu_make.pop()
            print("2")
            print(menu_make)
            f = open(namefile)
            for row in f:
                menu_make.append(row)
            f.close()
            print("3")
            print(menu_make)

        def insert():
            self.listTree.delete(*self.listTree.get_children())
            sum_price = 0
            No_pay = 0
            Qrder_quantity={"DeluxeVeggie":int(0),"VegVaganza":int(0),"5Pepper":int(0),"Margherita":int(0),"FishHeadSoup":int(0),"SpinachWith3Eggs":int(0),"ClearSoupwithBeanCurd":int(0),"SpicyCatfish":int(0),"FieryPorkRibsBroth":int(0),
    "SpicyMushroomSoup":int(0),"ShrimpCakes":int(0),"FriedFish-pasteBalls":int(0),"FriedChickenwithFishSauce":int(0),"FriedSunDriedPork":int(0),
    "FriedChineseChives":int(0),"FriedDumplings":int(0),"StirFriedPorkLiverwithChineseChives":int(0),"StirFriedPorkwithShrimpPaste":int(0),"StirFriedPorkLiverwithChili":int(0),"StirFriedB.EggwithBasil":int(0),
    "SpicyStirFriedCatfish":int(0),"FriedTofuandPrawnSauce":int(0),"SpicySalmonSalad":int(0),"SaltedEggSpicySalad":int(0),"SpicyCockleSalad":int(0),"ShrimpSalad":int(0),"BlueCrabSalad":int(0),"SpicySeafoodSalad":int(0),
    "PorkSatay":int(0),"StickyRice":int(0),"CookedRice":int(0),"LargeCookedRice":int(0),"GreenCurry":int(0),"PanangCurry":int(0),"KaengTaePo":int(0),"FishOrgansSourSoup":int(0),"KaengOom":int(0),"MassamanCurry":int(0)}
            for x in range(0,len(menu_make)):
                split_word = menu_make[x].split(",")
                print(split_word)
                word_in= ["","","","","","",""]
                for i in range(0,len(split_word)):
                    for w in split_word[i]:
                        if(w == "," or w == " " or w == "'"  or w == "]" or w == "["):  
                            pass
                        else:
                            word_in[i] += str(w)
                self.listTree.insert("", 'end', text=word_in[0], values=(word_in[1], word_in[2], word_in[3], word_in[4],word_in[6],word_in[5]))
                print(word_in[1])
                Qrder_quantity.update({word_in[1]:Qrder_quantity.get(word_in[1])+int(word_in[3])})
                print(Qrder_quantity)

                if(word_in[6][0]+word_in[6][1]+word_in[6][2]=="Yes"):   
                    sum_price+=int(word_in[4])
                else:
                    No_pay+=int(word_in[4])
            print(sum_price)
            print(No_pay)
            l5 = Label(self, text="Paid : "+str(sum_price),bg="#f2da9d",width=20,font=("Cooper Black",12)).place(x=20, y=550)
            l6 = Label(self, text="No paid : "+str(No_pay),bg="#f2da9d",width=20,font=("Cooper Black",12)).place(x=20, y=520)
            
            
            print("TOP SELL")
            print(Qrder_quantity)
            arr = []
            for k,v in Qrder_quantity.items():
                arr.append(v)
            print(arr)

            for i in range(1, len(arr)):

                key = arr[i]


                j = i-1
                while j >=0 and key < arr[j] :
                        arr[j+1] = arr[j]
                        j -= 1
                arr[j+1] = key


           
            for i in range(len(arr)):
                print ("%d" %arr[i])
            arr.reverse()
            print(arr)
            print(Qrder_quantity)
            top_sell_1 = list (Qrder_quantity.keys())[list(Qrder_quantity.values()).index(arr[0])]
            print(top_sell_1 )
            l6 =Label(self,text="TOP 1 : "+str(top_sell_1) + f"({arr[0]})",bg="#f2da9d",width=24,font=("Algerian",10,'bold')).place(x=300, y=530)


        def ge():
            if (len(m.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(d.get())) <= 0:
                messagebox.showinfo('Error', 'Enter the Day')
            elif (len(y.get())) <= 0:
                messagebox.showinfo('Error', 'Enter the Year')
            else:
                try:
                    month = m.get()
                    day = d.get()
                    year = y.get()
                    namefile = day + "_" +  month + "_" + year + ".txt"
                    print(namefile)
                    file_exists = os.path.exists(namefile)
                    if(file_exists==True):
                        up_load_data_make(namefile)
                        insert()
                        # TOP_SELL_1_2_3()
                    else:
                        messagebox.showinfo('Error', 'No information available for this date')
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            
        b=Button(self,text="Find",width=15,font=("Arial",10,'bold'),command=ge).place(x=460,y=200)
        c=ttk.Combobox(self,textvariable=m,values=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=d,width=43).place(x=180,y=155)
        en2 = Entry(self,textvariable=y,width=43).place(x=180,y=205)
        

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=12,columns=('Food Name', 'Type', 'Amount','Price','Pay','Time'))
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
        self.listTree.place(x=10, y=250)
        self.vsb.place(x=975,y=250,height=400)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))
       
        


Sea().mainloop()