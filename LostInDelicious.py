from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox
from tkinter import ttk
import os
import sys
py=sys.executable

class LostInDelicious:
    Qrder_quantity={"Fish Head Soup":0,"Spinach With 3 Eggs":0,"Clear Soup with Bean Curd":0,"Spicy Catfish":0,"Fiery Pork Ribs Broth":0,
    "Spicy Mushroom Soup":0,"Shrimp Cakes":0,"Fried Fish-paste Balls":0,"Fried Chicken with Fish Sauce":0,"Fried Sun Dried Pork":0,
    "Fried Chinese Chives":0,"Fried Dumplings":0,"Stir Fried Pork Liver with Chinese Chives":0,"Stir Fried Pork with Shrimp Paste":0,"Stir Fried Pork Liver with Chili":0,"Stir Fried B.Egg with Basil":0,
    "Spicy Stir Fried Catfish":0,"Fried Tofu and Prawn Sauce":0,"Spicy Salmon Salad":0,"Salted Egg Spicy Salad":0,"Spicy Cockle Salad":0,"Shrimp Salad":0,"Blue Crab Salad":0,"Spicy Seafood Salad":0,
    "Pork Satay":0,"Sticky Rice":0,"Cooked Rice":0,"Large Cooked Rice":0,"Green Curry":0,"Panang Curry":0,"Kaeng Tae Po":0,"Fish Organs Sour Soup":0,"Kaeng Oom":0,"Massaman Curry":0}

    Qrder_image={"Fish Head Soup":"newSoupFishHead.png","Spinach With 3 Eggs":"newThreeEggSoup.png","Clear Soup with Bean Curd":"newTomJued.png","Spicy Catfish":"newTomPlakang.png","Fiery Pork Ribs Broth":"newTomSaeb.png",
    "Spicy Mushroom Soup":"newTomYumHed.png","Shrimp Cakes":"newTodMunGung.png","Fried Fish-paste Balls":"newTodMunPla.png","Fried Chicken with Fish Sauce":"newChickenFishSauce.png","Fried Sun Dried Pork":"newOneLightPork.png",
    "Fried Chinese Chives":"newFryGuiCai.png","Fried Dumplings":"newFryGiow.png","Stir Fried Pork Liver with Chinese Chives":"newTubGuicai.png","Stir Fried Pork with Shrimp Paste":"newMuGapi.png","Stir Fried Pork Liver with Chili":"newTubPrik.png","Stir Fried B.Egg with Basil":"newKaiyeow.png",
    "Spicy Stir Fried Catfish":"newKangFish.png","Fried Tofu and Prawn Sauce":"newTofu.png","Spicy Salmon Salad":"newYumSalmon.png","Salted Egg Spicy Salad":"newYumMuyorKhaikem.png","Spicy Cockle Salad":"newYumHoi.png","Shrimp Salad":"newYumKung.png","Blue Crab Salad":"newYumPuu.png","Spicy Seafood Salad":"newYumSeaMix.png",
    "Pork Satay":"newMuSatae.png","Sticky Rice":"newKhaoNiow.png","Cooked Rice":"newKhaoJaan.png","Large Cooked Rice":"newKhaoTow.png","Green Curry":"newGangGreen.png","Panang Curry":"newGangPanaeng.png","Kaeng Tae Po":"newTaePo.png","Fish Organs Sour Soup":"newTaiPla.png","Kaeng Oom":"newGangUmm.png","Massaman Curry":"newMusmun.png"}
    
    cartlist=[]
    amount=0
    id = 0
    f = open("id.txt")
    for row in f:
        id = int(row)+1
    print(id)
#------ page 1 ------
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
            
        except:
            try:
                sf.scr=Tk()
            except:
                pass

        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #sf.scr.resizable(False, False)
        sf.scr.iconbitmap('icon.ico')
        sf.mainf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="banner.png")
        sf.l=Label(sf.mainf1,image=sf.logo)
        sf.l.place(x=0,y=0)
        sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.mainf2,height=618,width=1366)
        sf.c.pack()
        sf.back=PhotoImage(file="bg.png")
        sf.c.create_image(683,284,image=sf.back)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.mainf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=51)
        sf.lab=Button(sf.mainf2,text= "Enter the Restaurant",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("cooper black",30, 'bold'),fg="white",bg="#0b1335")
    
        sf.lab.place(x=450,y=250)
        sf.mainf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()


#------ page 2 ------
    def Login(sf):
        sf.up_load_data_order()

        sf.cartlist=[]
        sf.amount=0
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.loginf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.loginf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.loginf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=1010,y=100)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=51)

        sf.loginf1.pack(fill=BOTH,expand=1)
        sf.loginf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.loginf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.loginf2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=26,font=("cooper black",27))
        sf.log.place(x=59,y=105)
        sf.lab1=Label(sf.loginf2,text="UserName",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=100,y=180)
        sf.user=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=6 ,justify='left')
        sf.user.place(x=320,y=180)
        sf.lab2=Label(sf.loginf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=105,y=250)
        sf.pasd=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=6 ,justify='left', show = "*")
        sf.pasd.place(x=320,y=250)
        sf.lg=Button(sf.loginf2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.lg.place(x=180,y=320)
        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)
        sf.cl=Button(sf.loginf2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.cl.place(x=450,y=320)
        sf.rg=Button(sf.loginf2,text="For New Staff",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("cooper black",20),bd=6)
        sf.rg.place(x=270,y=390)
        sf.c.create_rectangle(850,120,1310,480,fill="#DC8076",outline="white",width=4)

        arr = []
        for k,v in sf.Qrder_quantity.items():
            arr.append(v)

        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        for i in range(len(arr)):
            print ("% d" % arr[i]),
        top_sell = list ( sf.Qrder_quantity.keys())[list(sf.Qrder_quantity.values()).index(arr[-1])]
        print(top_sell)

        top_sell = '''{}'''.format(top_sell)

        name_image =  sf.Qrder_image.get(top_sell)
        print(name_image)

        sf.ext=PhotoImage(file=name_image)
        sf.url=Label(sf.loginf2,image=sf.ext,cursor="hand2").place(x=955,y=125)
        sf.wtop1=Label(sf.loginf2,text="Best Selling Menu",bg="#DC8076",font=("cooper black",22))
        sf.wtop1.place(x=940,y=310)
        
        sf.T = Text(sf.loginf2, height = 2, width = 30,font=("cooper black",16),bg="white")
        sf.T.place(x=880,y=370)
        sf.T.tag_configure("tag_name", justify='center')
        sf.T.insert('end',top_sell)
        sf.T.tag_add("tag_name", "1.0", "end")
        sf.T.config(state='disabled')
        
        sf.loginf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass


#------ page 3 ------
    def Register(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.regf1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.regf1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.regf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=1010,y=100)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.regf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=51)
        sf.regf1.pack(fill=BOTH,expand=1)
        
        sf.regf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.regf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.regf2,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("cooper black",27))
        sf.log.place(x=480,y=120)
        sf.lab1=Label(sf.regf2,text="FirstName",bg="#d3ede6",font=("cooper black",18))
        sf.lab1.place(x=190,y=200)
        sf.first=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.first.place(x=430,y=200)
        sf.lab2=Label(sf.regf2,text="LastName",bg="#d3ede6",font=("cooper black",18))
        sf.lab2.place(x=730,y=200)
        sf.last=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.last.place(x=920,y=200)
        sf.lab3=Label(sf.regf2,text="Username",bg="#d3ede6",font=("cooper black",18))
        sf.lab3.place(x=190,y=250)
        sf.usern=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.usern.place(x=430,y=250)
        sf.lab4=Label(sf.regf2,text="Password",bg="#d3ede6",font=("cooper black",18))
        sf.lab4.place(x=730,y=250)
        sf.passd=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.passd.place(x=920,y=250)
        sf.lab5=Label(sf.regf2,text="Email",bg="#d3ede6",font=("cooper black",18))
        sf.lab5.place(x=190,y=300)
        sf.email=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.email.place(x=430,y=300)
        sf.lab6=Label(sf.regf2,text="Mobile No.",bg="#d3ede6",font=("cooper black",18))
        sf.lab6.place(x=730,y=300)
        sf.mob=Entry(sf.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.mob.place(x=920,y=300)
        sf.bc=Button(sf.regf2,text="Back",cursor="hand2",command=lambda:sf.Login(),fg="white",bg="#0b1335",font=("cooper black",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.regf2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Regdatabase(),font=("cooper black",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)
        sf.cl=Button(sf.regf2,text="Clear",cursor="hand2",fg="white",bg="#0b1335",command=lambda:clear(sf),font=("cooper black",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.regf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob=sf.mob.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob



#------ page 4 ------       
    def menulist(sf,x): 
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.menuf1=Frame(sf.scr,height=150,width=1366) # banner
        sf.c=Canvas(sf.menuf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.menuf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.home=Button(sf.menuf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.menuf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1080,y=100)
        sf.adlog=Button(sf.menuf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=940,y=100)
        sf.sum=Button(sf.menuf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.menuf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        sf.menuf1.pack(fill=BOTH,expand=1)
        sf.menuf2=Frame(sf.scr,height=618,width=1366) # main frame
        sf.c=Canvas(sf.menuf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50, 20, 438.7, 300,fill="#d3ede6",outline="white",width=6) # เเถว 1 คอลัม 1
        sf.c.create_rectangle(488.7, 20, 877.4, 300,fill="#d3ede6",outline="white",width=6) # เเถว 1 คอลัม 2
        sf.c.create_rectangle(927.4, 20, 1316.1, 300,fill="#d3ede6",outline="white",width=6) # เเถว 1 คอลัม 3
        sf.c.create_rectangle(50, 320, 438.7, 600,fill="#d3ede6",outline="white",width=6) # เเถว 2 คอลัม 1
        sf.c.create_rectangle(488.7, 320, 877.4, 600,fill="#d3ede6",outline="white",width=6) # เเถว 2 คอลัม 2
        sf.c.create_rectangle(927.4, 320, 1316.1, 600,fill="#d3ede6",outline="white",width=6) # เเถว 2 คอลัม 3

        sf.gang=PhotoImage(file="GangUmm.png") # ภาพฝ่ายเเกง
        sf.c.create_image(244.35,130,image=sf.gang)
        sf.gangbut=Button(sf.menuf2,text="Curry",cursor="hand2",fg="white",command=lambda:sf.gangfood(sf.x),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.gangbut.place(x=200,y=230)

        sf.soup=PhotoImage(file="SoupFishHead.png") # ภาพฝ่ายต้ม
        sf.c.create_image(683.05,130,image=sf.soup)
        sf.soupbut=Button(sf.menuf2,text="Soup",cursor="hand2",fg="white",command=lambda:sf.soupfood(sf.x),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.soupbut.place(x=640,y=230)

        sf.stirfry=PhotoImage(file="MuGapi.png") # ภาพฝ่ายผัด
        sf.c.create_image(1121.75,130,image=sf.stirfry)
        sf.stirfrybut=Button(sf.menuf2,text="Stir Fry",cursor="hand2",fg="white",command=lambda:sf.stirfryfood(sf.x),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.stirfrybut.place(x=1070,y=230)

        sf.fry=PhotoImage(file="TodMunGung.png") # ภาพฝ่ายทอด
        sf.c.create_image(244.35,430,image=sf.fry)
        sf.frybut=Button(sf.menuf2,text="Fry",cursor="hand2",fg="white",command=lambda:sf.fryfood(sf.x),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.frybut.place(x=210,y=530)

        sf.yum=PhotoImage(file="YumMuyorKhaikem.png") # ภาพฝ่ายยำ
        sf.c.create_image(683.05,430,image=sf.yum)
        sf.yumbut=Button(sf.menuf2,text="Yum",cursor="hand2",fg="white",command=lambda:sf.yumfood(sf.x),bg="#0b1335",bd=5,font=("default",18,'bold')) # ยังไม่มีคำสั่ง
        sf.yumbut.place(x=650,y=530)

        sf.other=PhotoImage(file="KhaoTow.png") # ภาพฝ่ายอื่นๆ
        sf.c.create_image(1121.75,430,image=sf.other)
        sf.otherbut=Button(sf.menuf2,text="Others",cursor="hand2",fg="white",command=lambda:sf.otherfood(sf.x),bg="#0b1335",bd=5,font=("default",18,'bold')) # ยังไม่มีคำสั่ง
        sf.otherbut.place(x=1070,y=530)

        sf.menuf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------ page 5 ------
    def gangfood(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.gangf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.gangf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.gangf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.gangf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.gangf1.pack(fill=BOTH,expand=1)
        sf.home=Button(sf.gangf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.gangf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1070,y=100)
        sf.adlog=Button(sf.gangf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.sum=Button(sf.gangf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)

        sf.gangf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.gangf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.gangf2,text="Curry",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=640,y=4)
        sf.c.create_rectangle(50, 40, 1320, 540,fill="#d3ede6",outline="white",width=6)
        sf.q1=StringVar()
        sf.q2=StringVar()
        sf.q3=StringVar()
        sf.q4=StringVar()
        sf.q5=StringVar()
        sf.q6=StringVar()
        sf.q1.set("0")
        sf.q2.set("0")
        sf.q3.set("0")
        sf.q4.set("0")
        sf.q5.set("0")
        sf.q6.set("0")
        
        # menu 1
        sf.c.create_rectangle(50, 40, 685, 210,width=2) #กรอบ 1 1
        sf.c.create_rectangle(685, 40, 1320, 210,width=2) #กรอบ 1 2
        sf.gangmenu1=PhotoImage(file="newGangGreen.png")
        sf.c.create_image(175,125,image=sf.gangmenu1)
        sf.c.create_text(400,70,text="Green Curry",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,110,text="80฿/120฿",fill="#ff3838",font=("default",17))
        sf.v1=IntVar()
        sf.C11=Radiobutton(sf.gangf2,text = "Medium",value=10,variable=sf.v1)
        sf.C11.place(x=400,y=100)
        sf.C12 = Radiobutton(sf.gangf2, text = "Large",value = 20, variable =sf.v1)    
        sf.C12.place(x=500,y=100)
        sf.C11.configure(background="#d3ede6")
        sf.C12.configure(background="#d3ede6")

        sf.C11.select()
        sf.C11.deselect()    
        sf.C11.invoke()
        sf.c.create_text(350,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty1=Entry(sf.gangf2,textvariable=sf.q1,bg="#aae2d7",font=("default",12),width=4,) # กรอกจำนวน
        sf.qty1.place(x=410,y=140)
        sf.add1=Button(sf.gangf2,text="ADD",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=600,y=160)
        def addch1():
            if sf.v1.get()==10:
                ch1="Medium"
                pric1=80
            elif sf.v1.get()==20:
                ch1="Large"
                pric1=120
            sf.addlist(["Green Curry",ch1,sf.q1.get(),pric1*int(sf.q1.get())])
            
        # menu 2
        sf.c.create_rectangle(50, 210, 685, 376,width=2) #กรอบ 2 1
        sf.c.create_rectangle(685, 210, 1320, 376,width=2) #กรอบ 2 2
        sf.gangmenu2=PhotoImage(file="newGangPanaeng.png")
        sf.c.create_image(175,294,image=sf.gangmenu2)
        sf.c.create_text(400,240,text="Panang Curry",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,280,text="70฿/90฿",fill="#ff3838",font=("default",17,))
        sf.v2=IntVar()
        sf.C21=Radiobutton(sf.gangf2,text = "Medium",value=10,variable=sf.v2)
        sf.C21.place(x=400,y=270)
        sf.C22 = Radiobutton(sf.gangf2, text = "Large",value = 20, variable =sf.v2)
        sf.C22.place(x=500,y=270)

        sf.C21.configure(background="#d3ede6")
        sf.C22.configure(background="#d3ede6")
 
        sf.C21.select()
        sf.C21.deselect()    
        sf.C21.invoke()
        sf.c.create_text(350,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty2=Entry(sf.gangf2,textvariable=sf.q2,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty2.place(x=410,y=310)
        sf.add2=Button(sf.gangf2,text="ADD",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=600,y=325)
        def addch2():
            if sf.v2.get()==10:
                ch2="Medium"
                pric2=70
            elif sf.v2.get()==20:
                ch2="Large"
                pric2=90
            sf.addlist(["Panang Curry",ch2,sf.q2.get(),pric2*int(sf.q2.get())])

        # menu 3
        sf.c.create_rectangle(50, 376, 685, 540,width=2) #กรอบ 3 1
        sf.c.create_rectangle(685, 376, 1320, 540,width=2) #กรอบ 3 2
        sf.gangmenu3=PhotoImage(file="newGangUmm.png")
        sf.c.create_image(175,458,image=sf.gangmenu3)
        sf.c.create_text(380,410,text="Kaeng Oom",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,450,text="70฿/90฿",fill="#ff3838",font=("default",17))
        sf.v3=IntVar()
        sf.C31=Radiobutton(sf.gangf2,text = "Medium",value=10,variable=sf.v3)
        sf.C31.place(x=400,y=440)
        sf.C32 = Radiobutton(sf.gangf2, text = "Large",value = 20, variable =sf.v3)
        sf.C32.place(x=500,y=440)

        sf.C31.configure(background="#d3ede6")
        sf.C32.configure(background="#d3ede6")
   
        sf.C31.select()
        sf.C31.deselect()    
        sf.C31.invoke()

        sf.c.create_text(350,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty3=Entry(sf.gangf2,textvariable=sf.q3,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty3.place(x=410,y=480)

        sf.add3=Button(sf.gangf2,text="ADD",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=600,y=490)
        def addch3():
            if sf.v3.get()==10:
                ch3="Medium"
                pric3=70
            elif sf.v3.get()==20:
                ch3="Large"
                pric3=90

            sf.addlist(["Kaeng Oom",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            
        # menu 4
        sf.gangmenu4=PhotoImage(file="newMusmun.png")
        sf.c.create_image(810,125,image=sf.gangmenu4)
        sf.c.create_text(1050,70,text="Massaman Curry",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,110,text="60฿/80฿",fill="#ff3838",font=("default",17,))
        sf.v4=IntVar()
        sf.C41=Radiobutton(sf.gangf2,text = "Medium",value=10,variable=sf.v4)
        sf.C41.place(x=1035,y=100)
        sf.C42 = Radiobutton(sf.gangf2, text = "Large",value = 20, variable =sf.v4)
        sf.C42.place(x=1135,y=100)

        sf.C41.configure(background="#d3ede6")
        sf.C42.configure(background="#d3ede6")
  
        sf.C41.select()
        sf.C41.deselect()    
        sf.C41.invoke()
        
        sf.c.create_text(980,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty4=Entry(sf.gangf2,textvariable=sf.q4,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty4.place(x=1040,y=140)
    
        sf.add4=Button(sf.gangf2,text="ADD",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=1235,y=160)
        def addch4():
            if sf.v4.get()==10:
                ch4="Medium"
                pric4=60
            elif sf.v4.get()==20:
                ch4="Large"
                pric4=80
 
            sf.addlist(["Massaman Curry",ch4,sf.q4.get(), pric4*int(sf.q4.get())])

        # menu 5
        sf.gangmenu5=PhotoImage(file="newTaePo.png")
        sf.c.create_image(810,294,image=sf.gangmenu5)
        sf.c.create_text(1030,240,text="Kaeng Tae Po",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,280,text="70฿/90฿",fill="#ff3838",font=("default",17,))
        sf.v5=IntVar()
        sf.C51=Radiobutton(sf.gangf2,text = "Medium",value=10,variable=sf.v5)
        sf.C51.place(x=1035,y=270)
        sf.C52 = Radiobutton(sf.gangf2, text = "Large",value = 20, variable =sf.v5)
        sf.C52.place(x=1135,y=270)

        sf.C51.configure(background="#d3ede6")
        sf.C52.configure(background="#d3ede6")
 
        sf.C51.select()
        sf.C51.deselect()    
        sf.C51.invoke()
        
        sf.c.create_text(980,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty5=Entry(sf.gangf2,textvariable=sf.q5,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty5.place(x=1040,y=310)
    
        sf.add5=Button(sf.gangf2,text="ADD",command=lambda:addch5(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add5.place(x=1235,y=325)
        def addch5():
            if sf.v5.get()==10:
                ch5="Medium"
                pric5=70
            elif sf.v5.get()==20:
                ch5="Large"
                pric5=90

            sf.addlist(["Kaeng Tae Po",ch5,sf.q5.get(), pric5*int(sf.q5.get())])

        # menu 6
        sf.gangmenu6=PhotoImage(file="newTaiPla.png")
        sf.c.create_image(810,458,image=sf.gangmenu6)
        sf.c.create_text(1090,410,text="Fish Organs Sour Soup",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,450,text="65฿/100฿",fill="#ff3838",font=("default",17,))
        sf.v6=IntVar()
        sf.C61=Radiobutton(sf.gangf2,text = "Medium",value=10,variable=sf.v6)
        sf.C61.place(x=1035,y=440)
        sf.C62 = Radiobutton(sf.gangf2, text = "Large",value = 20, variable =sf.v6)
        sf.C62.place(x=1135,y=440)

        sf.C61.configure(background="#d3ede6")
        sf.C62.configure(background="#d3ede6")
 
        sf.C61.select()
        sf.C61.deselect()    
        sf.C61.invoke()
        
        sf.c.create_text(980,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty6=Entry(sf.gangf2,textvariable=sf.q6,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty6.place(x=1040,y=480)

        sf.add6=Button(sf.gangf2,text="ADD",command=lambda:addch6(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add6.place(x=1235,y=490)
        def addch6():
            if sf.v6.get()==10:
                ch6="Medium"
                pric6=65
            elif sf.v6.get()==20:
                ch6="Large"
                pric6=100
   
            sf.addlist(["Fish Organs Sour Soup",ch6,sf.q6.get(), pric6*int(sf.q6.get())])


        sf.con=Button(sf.gangf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=550)
        sf.more=Button(sf.gangf2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=410,y=550)
        sf.bcancel=Button(sf.gangf2,text="Cancel",command=lambda:sf.cancel(sf),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.bcancel.place(x=630,y=550)
        sf.gangf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

        
    def cancel(sf,x):
        print(sf.cartlist)
        for i in range(0,len(sf.cartlist)):
            sf.cartlist.pop()
        print(sf.cartlist)

    def addlist(sf,q):
        if q[-2]!="0" and q[-2].isdigit():
            sf.amount=sf.amount+q[-1]
            q.insert(0, sf.id)
            # q.append(sf.id)
            x= time.asctime(time.localtime(time.time()))
            x = x.split(" ")
            print(x)
            timer = x[3]+"-"+x[2]+"-"+x[1]+"-"+x[4]
            q.append(timer)
            q.append("No")
            sf.cartlist.append(q)
            messagebox.showinfo("Cart","Item Successfully added")
            #update_id_to.txt
            with open("id.txt", "w", encoding="utf8") as f:
                f.write(str(sf.id))
        else:
            messagebox.showinfo("Cart","Enter Valid Quantity to add")
        print(sf.cartlist,sf.amount)


#--  page 6------
    def soupfood(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.soupf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.soupf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.soupf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.soupf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.soupf1.pack(fill=BOTH,expand=1)
        sf.home=Button(sf.soupf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.soupf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1070,y=100)
        sf.adlog=Button(sf.soupf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.sum=Button(sf.soupf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)


        sf.soupf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.soupf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.soupf2,text="Soup",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=645,y=4)
        sf.c.create_rectangle(50, 40, 1320, 540,fill="#d3ede6",outline="white",width=6)
        sf.q7=StringVar()
        sf.q8=StringVar()
        sf.q9=StringVar()
        sf.q10=StringVar()
        sf.q11=StringVar()
        sf.q12=StringVar()
        sf.q7.set("0")
        sf.q8.set("0")
        sf.q9.set("0")
        sf.q10.set("0")
        sf.q11.set("0")
        sf.q12.set("0")
        
        # menu 7
        sf.c.create_rectangle(50, 40, 685, 210,width=2) #กรอบ 1 1
        sf.c.create_rectangle(685, 40, 1320, 210,width=2) #กรอบ 1 2
        sf.soupmenu1=PhotoImage(file="newSoupFishHead.png")
        sf.c.create_image(175,125,image=sf.soupmenu1)
        sf.c.create_text(400,70,text="Fish Head Soup",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,110,text="120฿/150฿",fill="#ff3838",font=("default",17))
        sf.v7=IntVar()
        sf.C71=Radiobutton(sf.soupf2,text = "Medium",value=10,variable=sf.v7)
        sf.C71.place(x=400,y=100)
        sf.C72 = Radiobutton(sf.soupf2, text = "Large",value = 20, variable =sf.v7)    
        sf.C72.place(x=500,y=100)

        sf.C71.configure(background="#d3ede6")
        sf.C72.configure(background="#d3ede6")
  
        sf.C71.select()
        sf.C71.deselect()    
        sf.C71.invoke()
        sf.c.create_text(350,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty7=Entry(sf.soupf2,textvariable=sf.q7,bg="#aae2d7",font=("default",12),width=4,) # กรอกจำนวน
        sf.qty7.place(x=410,y=140)
        sf.add7=Button(sf.soupf2,text="ADD",command=lambda:addch7(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add7.place(x=600,y=160)
        def addch7():
            if sf.v7.get()==10:
                ch7="Medium"
                pric7=120
            elif sf.v7.get()==20:
                ch7="Large"
                pric7=150
     
            sf.addlist(["Fish Head Soup",ch7,sf.q7.get(),pric7*int(sf.q7.get())])
            
        # menu 8
        sf.c.create_rectangle(50, 210, 685, 376,width=2) #กรอบ 2 1
        sf.c.create_rectangle(685, 210, 1320, 376,width=2) #กรอบ 2 2
        sf.soupmenu2=PhotoImage(file="newThreeEggSoup.png")
        sf.c.create_image(175,294,image=sf.soupmenu2)
        sf.c.create_text(440,240,text="Spinach With 3 Eggs",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,280,text="100฿/120฿",fill="#ff3838",font=("default",17,))
        sf.v8=IntVar()
        sf.C81=Radiobutton(sf.soupf2,text = "Medium",value=10,variable=sf.v8)
        sf.C81.place(x=400,y=270)
        sf.C82 = Radiobutton(sf.soupf2, text = "Large",value = 20, variable =sf.v8)
        sf.C82.place(x=500,y=270)
  
        sf.C81.configure(background="#d3ede6")
        sf.C82.configure(background="#d3ede6")

        sf.C81.select()
        sf.C81.deselect()    
        sf.C81.invoke()
        sf.c.create_text(350,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty8=Entry(sf.soupf2,textvariable=sf.q8,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty8.place(x=410,y=310)
        sf.add8=Button(sf.soupf2,text="ADD",command=lambda:addch8(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add8.place(x=600,y=325)
        def addch8():
            if sf.v8.get()==10:
                ch8="Medium"
                pric8=100
            elif sf.v8.get()==20:
                ch8="Large"
                pric8=120
      
            sf.addlist(["Spinach With 3 Eggs",ch8,sf.q8.get(),pric8*int(sf.q8.get())])

        # menu 9  
        sf.c.create_rectangle(50, 376, 685, 540,width=2) #กรอบ 3 1
        sf.c.create_rectangle(685, 376, 1320, 540,width=2) #กรอบ 3 2
        sf.soupmenu3=PhotoImage(file="newTomJued.png")
        sf.c.create_image(175,458,image=sf.soupmenu3)
        sf.c.create_text(480,410,text="Clear Soup with Bean Curd",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,450,text="80฿/100฿",fill="#ff3838",font=("default",17))
        sf.v9=IntVar()
        sf.C91=Radiobutton(sf.soupf2,text = "Medium",value=10,variable=sf.v9)
        sf.C91.place(x=400,y=440)
        sf.C92 = Radiobutton(sf.soupf2, text = "Large",value = 20, variable =sf.v9)
        sf.C92.place(x=500,y=440)
    
        sf.C91.configure(background="#d3ede6")
        sf.C92.configure(background="#d3ede6")
    
        sf.C91.select()
        sf.C91.deselect()    
        sf.C91.invoke()

        sf.c.create_text(350,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty9=Entry(sf.soupf2,textvariable=sf.q9,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty9.place(x=410,y=480)

        sf.add9=Button(sf.soupf2,text="ADD",command=lambda:addch9(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add9.place(x=600,y=490)
        def addch9():
            if sf.v9.get()==10:
                ch9="Medium"
                pric9=80
            elif sf.v9.get()==20:
                ch9="Large"
                pric9=100
       
            sf.addlist(["Clear Soup with Bean Curd",ch9,sf.q9.get(),pric9*int(sf.q9.get())])
            
        # menu 10
     
        sf.soupmenu4=PhotoImage(file="newTomPlakang.png")
        sf.c.create_image(810,125,image=sf.soupmenu4)
        sf.c.create_text(1030,70,text="Spicy Catfish",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,110,text="200฿/230฿",fill="#ff3838",font=("default",17,))
   
        sf.v10=IntVar()
        sf.C101=Radiobutton(sf.soupf2,text = "Medium",value=10,variable=sf.v10)
        sf.C101.place(x=1035,y=100)
        sf.C102 = Radiobutton(sf.soupf2, text = "Large",value = 20, variable =sf.v10)
        sf.C102.place(x=1135,y=100)
     
        sf.C101.configure(background="#d3ede6")
        sf.C102.configure(background="#d3ede6")
    
        sf.C101.select()
        sf.C101.deselect()    
        sf.C101.invoke()
        
        sf.c.create_text(980,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty10=Entry(sf.soupf2,textvariable=sf.q10,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty10.place(x=1040,y=140)
    
        sf.add10=Button(sf.soupf2,text="ADD",command=lambda:addch10(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add10.place(x=1235,y=160)
        def addch10():
            if sf.v10.get()==10:
                ch10="Medium"
                pric10=200
            elif sf.v10.get()==20:
                ch10="Large"
                pric10=230
     
            sf.addlist(["Spicy Catfish",ch10,sf.q10.get(), pric10*int(sf.q10.get())])

        # menu 11
    
        sf.soupmenu5=PhotoImage(file="newTomSaeb.png")
        sf.c.create_image(810,294,image=sf.soupmenu5)
        sf.c.create_text(1090,240,text="Fiery Pork Ribs Broth",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,280,text="80฿/100฿",fill="#ff3838",font=("default",17,))
  
        sf.v11=IntVar()
        sf.C111=Radiobutton(sf.soupf2,text = "Medium",value=10,variable=sf.v11)
        sf.C111.place(x=1035,y=270)
        sf.C112 = Radiobutton(sf.soupf2, text = "Large",value = 20, variable =sf.v11)
        sf.C112.place(x=1135,y=270)
    
        sf.C111.configure(background="#d3ede6")
        sf.C112.configure(background="#d3ede6")
      
        sf.C111.select()
        sf.C111.deselect()    
        sf.C111.invoke()
        
        sf.c.create_text(980,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty11=Entry(sf.soupf2,textvariable=sf.q11,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty11.place(x=1040,y=310)
    
        sf.add11=Button(sf.soupf2,text="ADD",command=lambda:addch11(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add11.place(x=1235,y=325)
        def addch11():
            if sf.v11.get()==10:
                ch11="Medium"
                pric11=80
            elif sf.v11.get()==20:
                ch11="Large"
                pric11=100
   
            sf.addlist(["Fiery Pork Ribs Broth",ch11,sf.q11.get(), pric11*int(sf.q11.get())])

        # menu 12
    
        sf.soupmenu6=PhotoImage(file="newTomYumHed.png")
        sf.c.create_image(810,458,image=sf.soupmenu6)
        sf.c.create_text(1090,410,text="Spicy Mushroom Soup",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,450,text="95฿/120฿",fill="#ff3838",font=("default",17,))
     
        sf.v12=IntVar()
        sf.C121=Radiobutton(sf.soupf2,text = "Medium",value=10,variable=sf.v12)
        sf.C121.place(x=1035,y=440)
        sf.C122 = Radiobutton(sf.soupf2, text = "Large",value = 20, variable =sf.v12)
        sf.C122.place(x=1135,y=440)
    
        sf.C121.configure(background="#d3ede6")
        sf.C122.configure(background="#d3ede6")
      
        sf.C121.select()
        sf.C121.deselect()    
        sf.C121.invoke()
        
        sf.c.create_text(980,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty12=Entry(sf.soupf2,textvariable=sf.q12,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty12.place(x=1040,y=480)

        sf.add12=Button(sf.soupf2,text="ADD",command=lambda:addch12(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add12.place(x=1235,y=490)
        def addch12():
            if sf.v12.get()==10:
                ch12="Medium"
                pric12=95
            elif sf.v12.get()==20:
                ch12="Large"
                pric12=120
      
            sf.addlist(["Spicy Mushroom Soup",ch12,sf.q12.get(), pric12*int(sf.q12.get())])


        sf.con=Button(sf.soupf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=550)
        sf.more=Button(sf.soupf2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=410,y=550)
        sf.bcancel=Button(sf.soupf2,text="Cancel",command=lambda:sf.cancel(sf),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.bcancel.place(x=630,y=550)
        sf.soupf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()        

    

#--  page 7------
    def stirfryfood(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.stirfryf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.stirfryf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.stirfryf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.stirfryf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.stirfryf1.pack(fill=BOTH,expand=1)
        sf.home=Button(sf.stirfryf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.stirfryf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1070,y=100)
        sf.adlog=Button(sf.stirfryf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.sum=Button(sf.stirfryf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)

        sf.stirfryf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.stirfryf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.stirfryf2,text="Stir Fry",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=630,y=4)
        sf.c.create_rectangle(50, 40, 1320, 540,fill="#d3ede6",outline="white",width=6)
        sf.q13=StringVar()
        sf.q14=StringVar()
        sf.q15=StringVar()
        sf.q16=StringVar()
        sf.q17=StringVar()
        sf.q18=StringVar()
        sf.q13.set("0")
        sf.q14.set("0")
        sf.q15.set("0")
        sf.q16.set("0")
        sf.q17.set("0")
        sf.q18.set("0")
        
        # menu 13
        sf.c.create_rectangle(50, 40, 685, 210,width=2) #กรอบ 1 1
        sf.c.create_rectangle(685, 40, 1320, 210,width=2) #กรอบ 1 2
        sf.stirfrymenu1=PhotoImage(file="newKaiyeow.png")
        sf.c.create_image(175,125,image=sf.stirfrymenu1)
        sf.c.create_text(450,70,text="Stir Fried B.Egg with Basil",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(345,110,text="60฿/80฿",fill="#ff3838",font=("default",17))
        sf.v13=IntVar()
        sf.C131=Radiobutton(sf.stirfryf2,text = "Medium",value=10,variable=sf.v13)
        sf.C131.place(x=400,y=100)
        sf.C132 = Radiobutton(sf.stirfryf2, text = "Large",value = 20, variable =sf.v13)    
        sf.C132.place(x=500,y=100)
    
        sf.C131.configure(background="#d3ede6")
        sf.C132.configure(background="#d3ede6")
    
        sf.C131.select()
        sf.C131.deselect()    
        sf.C131.invoke()
        sf.c.create_text(350,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty13=Entry(sf.stirfryf2,textvariable=sf.q13,bg="#aae2d7",font=("default",12),width=4,) # กรอกจำนวน
        sf.qty13.place(x=410,y=140)
        sf.add13=Button(sf.stirfryf2,text="ADD",command=lambda:addch13(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add13.place(x=600,y=160)
        def addch13():
            if sf.v13.get()==10:
                ch13="Medium"
                pric13=60
            elif sf.v13.get()==20:
                ch13="Large"
                pric13=80
       
            sf.addlist(["Stir Fried B.Egg with Basil",ch13,sf.q13.get(),pric13*int(sf.q13.get())])
            
        # menu 14 
        sf.c.create_rectangle(50, 210, 685, 376,width=2) #กรอบ 2 1
        sf.c.create_rectangle(685, 210, 1320, 376,width=2) #กรอบ 2 2
        sf.stirfrymenu2=PhotoImage(file="newKangFish.png")
        sf.c.create_image(175,294,image=sf.stirfrymenu2)
        sf.c.create_text(430,240,text="Spicy Stir Fried Catfish",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(345,280,text="120฿/150฿",fill="#ff3838",font=("default",17,))
        sf.v14=IntVar()
        sf.C141=Radiobutton(sf.stirfryf2,text = "Medium",value=10,variable=sf.v14)
        sf.C141.place(x=400,y=270)
        sf.C142 = Radiobutton(sf.stirfryf2, text = "Large",value = 20, variable =sf.v14)
        sf.C142.place(x=500,y=270)
  
        sf.C141.configure(background="#d3ede6")
        sf.C142.configure(background="#d3ede6")
  
        sf.C141.select()
        sf.C141.deselect()    
        sf.C141.invoke()
        sf.c.create_text(350,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty14=Entry(sf.stirfryf2,textvariable=sf.q14,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty14.place(x=410,y=310)
        sf.add14=Button(sf.stirfryf2,text="ADD",command=lambda:addch14(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add14.place(x=600,y=325)
        def addch14():
            if sf.v14.get()==10:
                ch14="Medium"
                pric14=120
            elif sf.v14.get()==20:
                ch14="Large"
                pric14=150
   
            sf.addlist(["Spicy Stir Fried Catfish",ch14,sf.q14.get(),pric14*int(sf.q14.get())])

        # menu 15
        sf.c.create_rectangle(50, 376, 685, 540,width=2) #กรอบ 3 1
        sf.c.create_rectangle(685, 376, 1320, 540,width=2) #กรอบ 3 2
        sf.stirfrymenu3=PhotoImage(file="newMuGapi.png")
        sf.c.create_image(175,458,image=sf.stirfrymenu3)
        sf.c.create_text(490,410,text="Stir Fried Pork with Shrimp Paste",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(345,450,text="85฿/100฿",fill="#ff3838",font=("default",17))
        sf.v15=IntVar()
        sf.C151=Radiobutton(sf.stirfryf2,text = "Medium",value=10,variable=sf.v15)
        sf.C151.place(x=400,y=440)
        sf.C152 = Radiobutton(sf.stirfryf2, text = "Large",value = 20, variable =sf.v15)
        sf.C152.place(x=500,y=440)
   
        sf.C151.configure(background="#d3ede6")
        sf.C152.configure(background="#d3ede6")
      
        sf.C151.select()
        sf.C151.deselect()    
        sf.C151.invoke()

        sf.c.create_text(350,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty15=Entry(sf.stirfryf2,textvariable=sf.q15,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty15.place(x=410,y=480)

        sf.add15=Button(sf.stirfryf2,text="ADD",command=lambda:addch15(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add15.place(x=600,y=490)
        def addch15():
            if sf.v15.get()==10:
                ch15="Medium"
                pric15=85
            elif sf.v15.get()==20:
                ch15="Large"
                pric15=100
    
            sf.addlist(["Stir Fried Pork with Shrimp Paste",ch15,sf.q15.get(),pric15*int(sf.q15.get())])
            
        # menu 16
        sf.stirfrymenu4=PhotoImage(file="newTofu.png")
        sf.c.create_image(810,125,image=sf.stirfrymenu4)
        sf.c.create_text(1090,70,text="Fried Tofu and Prawn Sauce",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(980,110,text="120฿/150฿",fill="#ff3838",font=("default",17,))
        sf.v16=IntVar()
        sf.C161=Radiobutton(sf.stirfryf2,text = "Medium",value=10,variable=sf.v16)
        sf.C161.place(x=1035,y=100)
        sf.C162 = Radiobutton(sf.stirfryf2, text = "Large",value = 20, variable =sf.v16)
        sf.C162.place(x=1135,y=100)
  
        sf.C161.configure(background="#d3ede6")
        sf.C162.configure(background="#d3ede6")
       
        sf.C161.select()
        sf.C161.deselect()    
        sf.C161.invoke()
        
        sf.c.create_text(980,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty16=Entry(sf.stirfryf2,textvariable=sf.q16,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty16.place(x=1040,y=140)
    
        sf.add16=Button(sf.stirfryf2,text="ADD",command=lambda:addch16(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add16.place(x=1235,y=160)
        def addch16():
            if sf.v16.get()==10:
                ch16="Medium"
                pric16=120
            elif sf.v16.get()==20:
                ch16="Large"
                pric16=150
      
            sf.addlist(["Fried Tofu and Prawn Sauce",ch16,sf.q16.get(), pric16*int(sf.q16.get())])

        # menu 17
        sf.stirfrymenu5=PhotoImage(file="newTubGuicai.png")
        sf.c.create_image(810,294,image=sf.stirfrymenu5)
        sf.c.create_text(1120,240,text="Stir Fried Pork Liver with Chinese Chives",fill="#000000",font=("Cooper Black",13))
        sf.c.create_text(980,280,text="85฿/100฿",fill="#ff3838",font=("default",17,))
   
        sf.v17=IntVar()
        sf.C171=Radiobutton(sf.stirfryf2,text = "Medium",value=10,variable=sf.v17)
        sf.C171.place(x=1035,y=270)
        sf.C172 = Radiobutton(sf.stirfryf2, text = "Large",value = 20, variable =sf.v17)
        sf.C172.place(x=1135,y=270)
    
        sf.C171.configure(background="#d3ede6")
        sf.C172.configure(background="#d3ede6")
     
        sf.C171.select()
        sf.C171.deselect()    
        sf.C171.invoke()
        
        sf.c.create_text(980,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty17=Entry(sf.stirfryf2,textvariable=sf.q17,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty17.place(x=1040,y=310)
    
        sf.add17=Button(sf.stirfryf2,text="ADD",command=lambda:addch17(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add17.place(x=1235,y=325)
        def addch17():
            if sf.v17.get()==10:
                ch17="Medium"
                pric17=85
            elif sf.v17.get()==20:
                ch17="Large"
                pric17=100
         
            sf.addlist(["Stir Fried Pork Liver with Chinese Chives",ch17,sf.q17.get(), pric17*int(sf.q17.get())])

        # menu 18
      
        sf.stirfrymenu6=PhotoImage(file="newTubPrik.png")
        sf.c.create_image(810,458,image=sf.stirfrymenu6)
        sf.c.create_text(1110,410,text="Stir Fried Pork Liver with Chili",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(980,450,text="60฿/80฿",fill="#ff3838",font=("default",17,))
  
        sf.v18=IntVar()
        sf.C181=Radiobutton(sf.stirfryf2,text = "Medium",value=10,variable=sf.v18)
        sf.C181.place(x=1035,y=440)
        sf.C182 = Radiobutton(sf.stirfryf2, text = "Large",value = 20, variable =sf.v18)
        sf.C182.place(x=1135,y=440)
  
        sf.C181.configure(background="#d3ede6")
        sf.C182.configure(background="#d3ede6")
      
        sf.C181.select()
        sf.C181.deselect()    
        sf.C181.invoke()
        
        sf.c.create_text(980,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty18=Entry(sf.stirfryf2,textvariable=sf.q18,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty18.place(x=1040,y=480)

        sf.add18=Button(sf.stirfryf2,text="ADD",command=lambda:addch18(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add18.place(x=1235,y=490)
        def addch18():
            if sf.v18.get()==10:
                ch18="Medium"
                pric18=60
            elif sf.v18.get()==20:
                ch18="Large"
                pric18=80
      
            sf.addlist(["Stir Fried Pork Liver with Chili",ch18,sf.q18.get(), pric18*int(sf.q18.get())])


        sf.con=Button(sf.stirfryf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=550)
        sf.more=Button(sf.stirfryf2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=410,y=550)
        sf.bcancel=Button(sf.stirfryf2,text="Cancel",command=lambda:sf.cancel(sf),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.bcancel.place(x=630,y=550)
        sf.stirfryf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()


#--  page 8------
    def fryfood(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.fryf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.fryf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.fryf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.fryf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.fryf1.pack(fill=BOTH,expand=1)
        sf.home=Button(sf.fryf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.fryf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1070,y=100)
        sf.adlog=Button(sf.fryf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.sum=Button(sf.fryf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)

        sf.fryf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.fryf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.fryf2,text="Fry",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=655,y=4)
        sf.c.create_rectangle(50, 40, 1320, 540,fill="#d3ede6",outline="white",width=6)
        sf.q19=StringVar()
        sf.q20=StringVar()
        sf.q21=StringVar()
        sf.q22=StringVar()
        sf.q23=StringVar()
        sf.q24=StringVar()
        sf.q19.set("0")
        sf.q20.set("0")
        sf.q21.set("0")
        sf.q22.set("0")
        sf.q23.set("0")
        sf.q24.set("0")
        
        # menu 19
        sf.c.create_rectangle(50, 40, 685, 210,width=2) #กรอบ 1 1
        sf.c.create_rectangle(685, 40, 1320, 210,width=2) #กรอบ 1 2
        sf.frymenu1=PhotoImage(file="newChickenFishSauce.png")
        sf.c.create_image(175,125,image=sf.frymenu1)
        sf.c.create_text(470,70,text="Fried Chicken with Fish Sauce",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(345,110,text="80฿/120฿",fill="#ff3838",font=("default",17))
        sf.v19=IntVar()
        sf.C191=Radiobutton(sf.fryf2,text = "Medium",value=10,variable=sf.v19)
        sf.C191.place(x=400,y=100)
        sf.C192 = Radiobutton(sf.fryf2, text = "Large",value = 20, variable =sf.v19)    
        sf.C192.place(x=500,y=100)
   
        sf.C191.configure(background="#d3ede6")
        sf.C192.configure(background="#d3ede6")
    
        sf.C191.select()
        sf.C191.deselect()    
        sf.C191.invoke()
        sf.c.create_text(350,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty19=Entry(sf.fryf2,textvariable=sf.q19,bg="#aae2d7",font=("default",12),width=4,) # กรอกจำนวน
        sf.qty19.place(x=410,y=140)
        sf.add19=Button(sf.fryf2,text="ADD",command=lambda:addch19(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add19.place(x=600,y=160)
        def addch19():
            if sf.v19.get()==10:
                ch19="Medium"
                pric19=80
            elif sf.v19.get()==20:
                ch19="Large"
                pric19=120
      
            sf.addlist(["Fried Chicken with Fish Sauce",ch19,sf.q19.get(),pric19*int(sf.q19.get())])
            
        # menu 20    
        sf.c.create_rectangle(50, 210, 685, 376,width=2) #กรอบ 2 1
        sf.c.create_rectangle(685, 210, 1320, 376,width=2) #กรอบ 2 2
        sf.frymenu2=PhotoImage(file="newFryGiow.png")
        sf.c.create_image(175,294,image=sf.frymenu2)
        sf.c.create_text(400,240,text="Fried Dumplings",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(345,280,text="60฿/80฿",fill="#ff3838",font=("default",17,))
  
        sf.v20=IntVar()
        sf.C201=Radiobutton(sf.fryf2,text = "Medium",value=10,variable=sf.v20)
        sf.C201.place(x=400,y=270)
        sf.C202 = Radiobutton(sf.fryf2, text = "Large",value = 20, variable =sf.v20)
        sf.C202.place(x=500,y=270)
     
        sf.C201.configure(background="#d3ede6")
        sf.C202.configure(background="#d3ede6")
    
        sf.C201.select()
        sf.C201.deselect()    
        sf.C201.invoke()
        sf.c.create_text(350,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty20=Entry(sf.fryf2,textvariable=sf.q20,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty20.place(x=410,y=310)
        sf.add20=Button(sf.fryf2,text="ADD",command=lambda:addch20(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add20.place(x=600,y=325)
        def addch20():
            if sf.v20.get()==10:
                ch20="Medium"
                pric20=60
            elif sf.v20.get()==20:
                ch20="Large"
                pric20=80
     
            sf.addlist(["Fried Dumplings",ch20,sf.q20.get(),pric20*int(sf.q20.get())])

        # menu 21
      
        sf.c.create_rectangle(50, 376, 685, 540,width=2) #กรอบ 3 1
        sf.c.create_rectangle(685, 376, 1320, 540,width=2) #กรอบ 3 2
        sf.frymenu3=PhotoImage(file="newFryGuiCai.png")
        sf.c.create_image(175,458,image=sf.frymenu3)
        sf.c.create_text(420,410,text="Fried Chinese Chives",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(345,450,text="50฿/70฿",fill="#ff3838",font=("default",17))
    
        sf.v21=IntVar()
        sf.C211=Radiobutton(sf.fryf2,text = "Medium",value=10,variable=sf.v21)
        sf.C211.place(x=400,y=440)
        sf.C212 = Radiobutton(sf.fryf2, text = "Large",value = 20, variable =sf.v21)
        sf.C212.place(x=500,y=440)
    
        sf.C211.configure(background="#d3ede6")
        sf.C212.configure(background="#d3ede6")
     
        sf.C211.select()
        sf.C211.deselect()    
        sf.C211.invoke()

        sf.c.create_text(350,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qrt21=Entry(sf.fryf2,textvariable=sf.q21,bg="#aae2d7",font=("default",12),width=4,)
        sf.qrt21.place(x=410,y=480)

        sf.add21=Button(sf.fryf2,text="ADD",command=lambda:addch21(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add21.place(x=600,y=490)
        def addch21():
            if sf.v21.get()==10:
                ch21="Medium"
                pric21=50
            elif sf.v21.get()==20:
                ch21="Large"
                pric21=70
      
            sf.addlist(["Fried Chinese Chives",ch21,sf.q21.get(),pric21*int(sf.q21.get())])
            
        # menu 22     
        sf.frymenu4=PhotoImage(file="newOneLightPork.png")
        sf.c.create_image(810,125,image=sf.frymenu4)
        sf.c.create_text(1060,70,text="Fried Sun Dried Pork",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(980,110,text="60฿/80฿",fill="#ff3838",font=("default",17,))
        sf.v22=IntVar()
        sf.C221=Radiobutton(sf.fryf2,text = "Medium",value=10,variable=sf.v22)
        sf.C221.place(x=1035,y=100)
        sf.C222 = Radiobutton(sf.fryf2, text = "Large",value = 20, variable =sf.v22)
        sf.C222.place(x=1135,y=100)
   
        sf.C221.configure(background="#d3ede6")
        sf.C222.configure(background="#d3ede6")
      
        sf.C221.select()
        sf.C221.deselect()    
        sf.C221.invoke()
        
        sf.c.create_text(980,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty22=Entry(sf.fryf2,textvariable=sf.q22,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty22.place(x=1040,y=140)
    
        sf.add22=Button(sf.fryf2,text="ADD",command=lambda:addch22(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add22.place(x=1235,y=160)
        def addch22():
            if sf.v22.get()==10:
                ch22="Medium"
                pric22=60
            elif sf.v22.get()==20:
                ch22="Large"
                pric22=80
         
            sf.addlist(["Fried Sun Dried Pork",ch22,sf.q22.get(), pric22*int(sf.q22.get())])

        # menu 23
        sf.frymenu5=PhotoImage(file="newTodMunGung.png")
        sf.c.create_image(810,294,image=sf.frymenu5)
        sf.c.create_text(1020,240,text="Shrimp Cakes",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(980,280,text="100฿/130฿",fill="#ff3838",font=("default",17,))
        sf.v23=IntVar()
        sf.C231=Radiobutton(sf.fryf2,text = "Medium",value=10,variable=sf.v23)
        sf.C231.place(x=1035,y=270)
        sf.C232 = Radiobutton(sf.fryf2, text = "Large",value = 20, variable =sf.v23)
        sf.C232.place(x=1135,y=270)
      
        sf.C231.configure(background="#d3ede6")
        sf.C232.configure(background="#d3ede6")
      
        sf.C231.select()
        sf.C231.deselect()    
        sf.C231.invoke()
        
        sf.c.create_text(980,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty23=Entry(sf.fryf2,textvariable=sf.q23,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty23.place(x=1040,y=310)
    
        sf.add23=Button(sf.fryf2,text="ADD",command=lambda:addch23(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add23.place(x=1235,y=325)
        def addch23():
            if sf.v23.get()==10:
                ch23="Medium"
                pric23=100
            elif sf.v23.get()==20:
                ch23="Large"
                pric23=130
    
            sf.addlist(["Shrimp Cakes",ch23,sf.q23.get(), pric23*int(sf.q23.get())])

        # menu 24  
        sf.frymenu6=PhotoImage(file="newTodMunPla.png")
        sf.c.create_image(810,458,image=sf.frymenu6)
        sf.c.create_text(1060,410,text="Fried Fish-paste Balls",fill="#000000",font=("Cooper Black",16))
        sf.c.create_text(980,450,text="100฿/120฿",fill="#ff3838",font=("default",17,))
        sf.v24=IntVar()
        sf.C241=Radiobutton(sf.fryf2,text = "Medium",value=10,variable=sf.v24)
        sf.C241.place(x=1035,y=440)
        sf.C242 = Radiobutton(sf.fryf2, text = "Large",value = 20, variable =sf.v24)
        sf.C242.place(x=1135,y=440)
    
        sf.C241.configure(background="#d3ede6")
        sf.C242.configure(background="#d3ede6")
     
        sf.C241.select()
        sf.C241.deselect()    
        sf.C241.invoke()
        
        sf.c.create_text(980,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty24=Entry(sf.fryf2,textvariable=sf.q24,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty24.place(x=1040,y=480)

        sf.add24=Button(sf.fryf2,text="ADD",command=lambda:addch24(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add24.place(x=1235,y=490)
        def addch24():
            if sf.v24.get()==10:
                ch24="Medium"
                pric24=100
            elif sf.v24.get()==20:
                ch24="Large"
                pric24=120
     
            sf.addlist(["Fried Fish-paste Balls",ch24,sf.q24.get(), pric24*int(sf.q24.get())])


        sf.con=Button(sf.fryf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=550)
        sf.more=Button(sf.fryf2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=410,y=550)
        sf.bcancel=Button(sf.fryf2,text="Cancel",command=lambda:sf.cancel(sf),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.bcancel.place(x=630,y=550)
        sf.fryf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 9------
    def yumfood(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.yumf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.yumf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.yumf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.yumf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.yumf1.pack(fill=BOTH,expand=1)
        sf.home=Button(sf.yumf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.yumf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1070,y=100)
        sf.adlog=Button(sf.yumf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.sum=Button(sf.yumf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)


        sf.yumf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.yumf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.yumf2,text="Yum",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=650,y=4)
        sf.c.create_rectangle(50, 40, 1320, 540,fill="#d3ede6",outline="white",width=6)
        sf.q25=StringVar()
        sf.q26=StringVar()
        sf.q27=StringVar()
        sf.q28=StringVar()
        sf.q29=StringVar()
        sf.q30=StringVar()
        sf.q25.set("0")
        sf.q26.set("0")
        sf.q27.set("0")
        sf.q28.set("0")
        sf.q29.set("0")
        sf.q30.set("0")
        
        # menu 25
        sf.c.create_rectangle(50, 40, 685, 210,width=2) #กรอบ 1 1
        sf.c.create_rectangle(685, 40, 1320, 210,width=2) #กรอบ 1 2
        sf.yummenu1=PhotoImage(file="newYumHoi.png")
        sf.c.create_image(175,125,image=sf.yummenu1)
        sf.c.create_text(440,70,text="Spicy Cockle Salad",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,110,text="160฿/200฿",fill="#ff3838",font=("default",17))
        sf.v25=IntVar()
        sf.C251=Radiobutton(sf.yumf2,text = "Medium",value=10,variable=sf.v25)
        sf.C251.place(x=400,y=100)
        sf.C252 = Radiobutton(sf.yumf2, text = "Large",value = 20, variable =sf.v25)    
        sf.C252.place(x=500,y=100)
  
        sf.C251.configure(background="#d3ede6")
        sf.C252.configure(background="#d3ede6")
     
        sf.C251.select()
        sf.C251.deselect()    
        sf.C251.invoke()
        sf.c.create_text(350,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty25=Entry(sf.yumf2,textvariable=sf.q25,bg="#aae2d7",font=("default",12),width=4,) # กรอกจำนวน
        sf.qty25.place(x=410,y=140)
        sf.add265=Button(sf.yumf2,text="ADD",command=lambda:addch25(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add265.place(x=600,y=160)
        def addch25():
            if sf.v25.get()==10:
                ch25="Medium"
                pric25=160
            elif sf.v25.get()==20:
                ch25="Large"
                pric25=200
     
            sf.addlist(["Spicy Cockle Salad",ch25,sf.q25.get(),pric25*int(sf.q25.get())])
            
        # menu 26   
        sf.c.create_rectangle(50, 210, 685, 376,width=2) #กรอบ 2 1
        sf.c.create_rectangle(685, 210, 1320, 376,width=2) #กรอบ 2 2
        sf.yummenu2=PhotoImage(file="newYumKung.png")
        sf.c.create_image(175,294,image=sf.yummenu2)
        sf.c.create_text(400,240,text="Shrimp Salad",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,280,text="200฿/230฿",fill="#ff3838",font=("default",17,))
        sf.v26=IntVar()
        sf.C261=Radiobutton(sf.yumf2,text = "Medium",value=10,variable=sf.v26)
        sf.C261.place(x=400,y=270)
        sf.C262 = Radiobutton(sf.yumf2, text = "Large",value = 20, variable =sf.v26)
        sf.C262.place(x=500,y=270)
   
        sf.C261.configure(background="#d3ede6")
        sf.C262.configure(background="#d3ede6")
     
        sf.C261.select()
        sf.C261.deselect()    
        sf.C261.invoke()
        sf.c.create_text(350,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty26=Entry(sf.yumf2,textvariable=sf.q26,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty26.place(x=410,y=310)
        sf.add26=Button(sf.yumf2,text="ADD",command=lambda:addch26(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add26.place(x=600,y=325)
        def addch26():
            if sf.v26.get()==10:
                ch26="Medium"
                pric26=200
            elif sf.v26.get()==20:
                ch26="Large"
                pric26=230
     
            sf.addlist(["Shrimp Salad",ch26,sf.q26.get(),pric26*int(sf.q26.get())])

        # menu 27    
        sf.c.create_rectangle(50, 376, 685, 540,width=2) #กรอบ 3 1
        sf.c.create_rectangle(685, 376, 1320, 540,width=2) #กรอบ 3 2
        sf.yummenu3=PhotoImage(file="newYumMuyorKhaikem.png")
        sf.c.create_image(175,458,image=sf.yummenu3)
        sf.c.create_text(460,410,text="Salted Egg Spicy Salad",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,450,text="140฿/170฿",fill="#ff3838",font=("default",17))
        sf.v27=IntVar()
        sf.C271=Radiobutton(sf.yumf2,text = "Medium",value=10,variable=sf.v27)
        sf.C271.place(x=400,y=440)
        sf.C272 = Radiobutton(sf.yumf2, text = "Large",value = 20, variable =sf.v27)
        sf.C272.place(x=500,y=440)
    
        sf.C271.configure(background="#d3ede6")
        sf.C272.configure(background="#d3ede6")
    
        sf.C271.select()
        sf.C271.deselect()    
        sf.C271.invoke()

        sf.c.create_text(350,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty27=Entry(sf.yumf2,textvariable=sf.q27,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty27.place(x=410,y=480)

        sf.add27=Button(sf.yumf2,text="ADD",command=lambda:addch27(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add27.place(x=600,y=490)
        def addch27():
            if sf.v27.get()==10:
                ch27="Medium"
                pric27=140
            elif sf.v27.get()==20:
                ch27="Large"
                pric27=170
  
            sf.addlist(["Salted Egg Spicy Salad",ch27,sf.q27.get(),pric27*int(sf.q27.get())])
            
        # menu 28
        sf.yummenu4=PhotoImage(file="newYumPuu.png")
        sf.c.create_image(810,125,image=sf.yummenu4)
        sf.c.create_text(1050,70,text="Blue Crab Salad",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,110,text="250฿/280฿",fill="#ff3838",font=("default",17,))
        sf.v28=IntVar()
        sf.C281=Radiobutton(sf.yumf2,text = "Medium",value=10,variable=sf.v28)
        sf.C281.place(x=1035,y=100)
        sf.C282 = Radiobutton(sf.yumf2, text = "Large",value = 20, variable =sf.v28)
        sf.C282.place(x=1135,y=100)
   
        sf.C281.configure(background="#d3ede6")
        sf.C282.configure(background="#d3ede6")
    
        sf.C281.select()
        sf.C281.deselect()    
        sf.C281.invoke()
        
        sf.c.create_text(980,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty28=Entry(sf.yumf2,textvariable=sf.q28,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty28.place(x=1040,y=140)
    
        sf.add28=Button(sf.yumf2,text="ADD",command=lambda:addch28(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add28.place(x=1235,y=160)
        def addch28():
            if sf.v28.get()==10:
                ch28="Medium"
                pric28=250
            elif sf.v28.get()==20:
                ch28="Large"
                pric28=280
      
            sf.addlist(["Blue Crab Salad",ch28,sf.q28.get(), pric28*int(sf.q28.get())])

        # menu 29 
        sf.yummenu5=PhotoImage(file="newYumSalmon.png")
        sf.c.create_image(810,294,image=sf.yummenu5)
        sf.c.create_text(1075,240,text="Spicy Salmon Salad",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,280,text="120฿/150฿",fill="#ff3838",font=("default",17,))
        sf.v29=IntVar()
        sf.C291=Radiobutton(sf.yumf2,text = "Medium",value=10,variable=sf.v29)
        sf.C291.place(x=1035,y=270)
        sf.C292 = Radiobutton(sf.yumf2, text = "Large",value = 20, variable =sf.v29)
        sf.C292.place(x=1135,y=270)
    
        sf.C291.configure(background="#d3ede6")
        sf.C292.configure(background="#d3ede6")
     
        sf.C291.select()
        sf.C291.deselect()    
        sf.C291.invoke()
        
        sf.c.create_text(980,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty29=Entry(sf.yumf2,textvariable=sf.q29,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty29.place(x=1040,y=310)
    
        sf.add29=Button(sf.yumf2,text="ADD",command=lambda:addch29(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add29.place(x=1235,y=325)
        def addch29():
            if sf.v29.get()==10:
                ch29="Medium"
                pric29=120
            elif sf.v29.get()==20:
                ch29="Large"
                pric29=150
            else:
                ch29="Regular"
                pric29=99
            sf.addlist(["Spicy Salmon Salad",ch29,sf.q29.get(), pric29*int(sf.q29.get())])

        # menu 30
        sf.yummenu6=PhotoImage(file="newYumSeaMix.png")
        sf.c.create_image(810,458,image=sf.yummenu6)
        sf.c.create_text(1080,410,text="Spicy Seafood Salad",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,450,text="300฿/350฿",fill="#ff3838",font=("default",17,))
        sf.v30=IntVar()
        sf.C301=Radiobutton(sf.yumf2,text = "Medium",value=10,variable=sf.v30)
        sf.C301.place(x=1035,y=440)
        sf.C302 = Radiobutton(sf.yumf2, text = "Large",value = 20, variable =sf.v30)
        sf.C302.place(x=1135,y=440)
     
        sf.C301.configure(background="#d3ede6")
        sf.C302.configure(background="#d3ede6")
    
        sf.C301.select()
        sf.C301.deselect()    
        sf.C301.invoke()
        
        sf.c.create_text(980,490,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty30=Entry(sf.yumf2,textvariable=sf.q30,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty30.place(x=1040,y=480)

        sf.add30=Button(sf.yumf2,text="ADD",command=lambda:addch30(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add30.place(x=1235,y=490)
        def addch30():
            if sf.v30.get()==10:
                ch30="Medium"
                pric30=300
            elif sf.v30.get()==20:
                ch30="Large"
                pric30=350
     
            sf.addlist(["Spicy Seafood Salad",ch30,sf.q30.get(), pric30*int(sf.q30.get())])


        sf.con=Button(sf.yumf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=550)
        sf.more=Button(sf.yumf2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=410,y=550)
        sf.bcancel=Button(sf.yumf2,text="Cancel",command=lambda:sf.cancel(sf),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.bcancel.place(x=630,y=550)
        sf.yumf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 10------
    def otherfood(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Lost In Delicious")
        w = 1366
        h = 768 
        ws = sf.scr.winfo_screenwidth() 
        hs = sf.scr.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2) -25
        sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
        sf.scr.iconbitmap('icon.ico')
        #sf.scr.resizable(False, False)
        sf.otherf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.otherf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="banner.png")
        sf.ba=Label(sf.otherf1,image=sf.logo,height=155).place(x=0,y=0)

        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.otherf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
        sf.tim.place(x=923,y=53)
        
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.otherf1.pack(fill=BOTH,expand=1)
        sf.home=Button(sf.otherf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("cooper black",16))
        sf.home.place(x=800,y=100)
        sf.mainmid=Button(sf.otherf1,text="Main",command=lambda:sf.midder_open(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.mainmid.place(x=1070,y=100)
        sf.adlog=Button(sf.otherf1,text="Receipt",command=lambda:sf.test_receipt(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=925,y=100)
        sf.sum=Button(sf.otherf1,text="Summary",command=lambda:sf.test_summary(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))  
        sf.sum.place(x=1190,y=100)


        sf.otherf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.otherf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="bg.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.otherf2,text="Others",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=635,y=4)
        sf.c.create_rectangle(50, 40, 1320, 376,fill="#d3ede6",outline="white",width=6)
        sf.q31=StringVar()
        sf.q32=StringVar()
        sf.q33=StringVar()
        sf.q34=StringVar()
        sf.q5=StringVar()
        sf.q6=StringVar()
        sf.q31.set("0")
        sf.q32.set("0")
        sf.q33.set("0")
        sf.q34.set("0")
        sf.q5.set("0")
        sf.q6.set("0")
        
        # menu 31
        sf.c.create_rectangle(50, 40, 685, 210,width=2) #กรอบ 1 1
        sf.c.create_rectangle(685, 40, 1320, 210,width=2) #กรอบ 1 2
        sf.othermenu1=PhotoImage(file="newKhaoJaan.png")
        sf.c.create_image(175,125,image=sf.othermenu1)
        sf.c.create_text(400,70,text="Cooked Rice",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,110,text="10฿",fill="#ff3838",font=("default",17))
        sf.v31=IntVar()
        sf.C311=Radiobutton(sf.otherf2,text = "Medium",value=10,variable=sf.v31)
        sf.C311.place(x=400,y=100)
  
        sf.C311.configure(background="#d3ede6")

        sf.C311.select()
        sf.C311.deselect()    
        sf.C311.invoke()
        sf.c.create_text(350,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty31=Entry(sf.otherf2,textvariable=sf.q31,bg="#aae2d7",font=("default",12),width=4,) # กรอกจำนวน
        sf.qty31.place(x=410,y=140)
        sf.add31=Button(sf.otherf2,text="ADD",command=lambda:addch31(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add31.place(x=600,y=160)
        def addch31():
            if sf.v31.get()==10:
                ch31="Medium"
                pric31=10

            sf.addlist(["Cooked Rice",ch31,sf.q31.get(),pric31*int(sf.q31.get())])
            
        # menu 32
        sf.c.create_rectangle(50, 210, 685, 376,width=2) #กรอบ 2 1
        sf.c.create_rectangle(685, 210, 1320, 376,width=2) #กรอบ 2 2
        sf.othermenu2=PhotoImage(file="newKhaoNiow.png")
        sf.c.create_image(175,294,image=sf.othermenu2)
        sf.c.create_text(400,240,text="Sticky Rice",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(345,280,text="15฿",fill="#ff3838",font=("default",17,))
        sf.v32=IntVar()
        sf.C321=Radiobutton(sf.otherf2,text = "Medium",value=10,variable=sf.v32)
        sf.C321.place(x=400,y=270)
     
        sf.C321.configure(background="#d3ede6")
 
        sf.C321.select()
        sf.C321.deselect()    
        sf.C321.invoke()
        sf.c.create_text(350,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty32=Entry(sf.otherf2,textvariable=sf.q32,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty32.place(x=410,y=310)
        sf.add32=Button(sf.otherf2,text="ADD",command=lambda:addch32(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add32.place(x=600,y=325)
        def addch32():
            if sf.v32.get()==10:
                ch32="Medium"
                pric32=15
    
            sf.addlist(["Sticky Rice",ch32,sf.q32.get(),pric32*int(sf.q32.get())])

        # menu 33
      
        sf.othermenu3=PhotoImage(file="newKhaoTow.png")
        sf.c.create_image(810,125,image=sf.othermenu3)
        sf.c.create_text(1080,70,text="Large Cooked Rice",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,110,text="60฿",fill="#ff3838",font=("default",17,))
        sf.v33=IntVar()
        sf.C331=Radiobutton(sf.otherf2,text = "Medium",value=10,variable=sf.v33)
        sf.C331.place(x=1035,y=100)
  
        sf.C331.configure(background="#d3ede6")
    
        sf.C331.select()
        sf.C331.deselect()    
        sf.C331.invoke()
        
        sf.c.create_text(980,150,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty33=Entry(sf.otherf2,textvariable=sf.q34,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty33.place(x=1040,y=140)
    
        sf.add33=Button(sf.otherf2,text="ADD",command=lambda:addch33(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add33.place(x=1235,y=160)
        def addch33():
            if sf.v33.get()==10:
                ch33="Medium"
                pric33=60
     
            sf.addlist(["Large Cooked Rice",ch33,sf.q34.get(), pric33*int(sf.q34.get())])

        # menu 34
      
        sf.othermenu4=PhotoImage(file="newMuSatae.png")
        sf.c.create_image(810,294,image=sf.othermenu4)
        sf.c.create_text(1030,240,text="Pork Satay",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(980,280,text="80฿/100฿",fill="#ff3838",font=("default",17,))
        sf.v34=IntVar()
        sf.C341=Radiobutton(sf.otherf2,text = "Medium",value=10,variable=sf.v34)
        sf.C341.place(x=1035,y=270)
        sf.C342 = Radiobutton(sf.otherf2, text = "Large",value = 20, variable =sf.v34)
        sf.C342.place(x=1135,y=270)
     
        sf.C341.configure(background="#d3ede6")
        sf.C342.configure(background="#d3ede6")
  
        sf.C341.select()
        sf.C341.deselect()    
        sf.C341.invoke()
        
        sf.c.create_text(980,320,text="Quantity : ",fill="#000000",font=("default",14))
        sf.qty34=Entry(sf.otherf2,textvariable=sf.q5,bg="#aae2d7",font=("default",12),width=4,)
        sf.qty34.place(x=1040,y=310)
    
        sf.add34=Button(sf.otherf2,text="ADD",command=lambda:addch34(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add34.place(x=1235,y=325)
        def addch34():
            if sf.v34.get()==10:
                ch34="Medium"
                pric34=80
            elif sf.v34.get()==20:
                ch34="Large"
                pric34=100
  
            sf.addlist(["Pork Satay",ch34,sf.q5.get(), pric34*int(sf.q5.get())])


        sf.con=Button(sf.otherf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        # sf.con=Button(sf.otherf2,text="Confirm Order",command=lambda:sf.Orderde(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=800,y=550)
        sf.more=Button(sf.otherf2,text="Add More..",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=410,y=550)
        sf.bcancel=Button(sf.otherf2,text="Cancel",command=lambda:sf.cancel(sf),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.bcancel.place(x=630,y=550)
        sf.otherf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

     
#--  page 11------
    def Orderde(sf,x):
        if(len(sf.cartlist)!=0):
            sf.midder_update()
            sf.x=x
            sf.scr.destroy()
            sf.scr=Tk()
            sf.scr.title("Lost In Delicious")
            w = 1366
            h = 768 
            ws = sf.scr.winfo_screenwidth() 
            hs = sf.scr.winfo_screenheight() 
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2) -25
            sf.scr.geometry('%dx%d+%d+%d' % (w, h, x, y))
            sf.scr.iconbitmap('icon.ico')
            #sf.scr.resizable(False, False)
            sf.ordf1=Frame(sf.scr,height=150,width=1366)
            sf.c=Canvas(sf.ordf1,height=150,width=1366)
            sf.c.pack()
            sf.logo=PhotoImage(file="banner.PNG")
            sf.c.create_image(683,75,image=sf.logo)
            sf.home=Button(sf.ordf1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
            sf.home.place(x=1000,y=90)
            sf.localtime=time.asctime(time.localtime(time.time()))
            sf.tim=Label(sf.ordf1,text=sf.localtime,fg="white",font=("default",16),bg="#416918")
            sf.tim.place(x=921,y=49)
            sf.ordf1.pack(fill=BOTH,expand=1)
            
            sf.ordf2=Frame(sf.scr,height=618,width=1366)
            sf.c=Canvas(sf.ordf2,height=618,width=1366)
            sf.c.pack()
            sf.logo1=PhotoImage(file="bg.png")
            sf.c.create_image(683,309,image=sf.logo1)
            sf.log=Label(sf.ordf2,text="YOUR ORDER",bg="#9db1f2",font=("Cooper Black",22))
            sf.log.place(x=450,y=4)
            sf.c.create_rectangle(250, 50, 800, 600,fill="#d3ede6",outline="white",width=6)
            sf.amt=sf.amount
            sf.text="Total : "+str(sf.amt)
            sf.tot=Label(sf.ordf2,text=sf.text,bg="#f2da9d",width=12,font=("Cooper Black",22))
            sf.tot.place(x=900,y=250)


            sf.exi=Button(sf.ordf2,text="New Order",command=lambda:sf.menulist(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
            sf.exi.place(x=900,y=300)
            sf.c.create_text(525,80,text="Items\tSize\tQty\tPrice",font=("cooper black",18))
            sf.c.create_text(525,90,text="_______________________________________",font=("cooper black",18))
            y=100
            for i in sf.cartlist:
                y+=30
                s=i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+str(i[4])
                sf.c.create_text(525,y,text=s,font=("default",16))
            sf.cartlist = []
            sf.ordf2.pack(fill=BOTH,expand=1)
            sf.scr.mainloop()
        else:
            messagebox.showinfo("","Please select your menu")

        
 #-----  database-------               
    def logindatabase(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("login_db.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
        if list(x)[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In\nWelcome to the Lost In Delicious")            
            sf.menulist("pick")
            

    def Regdatabase(sf):
        sf.credreg=sf.resultreg()
        sf.con=connect("login_db.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and mob=%r "%(sf.credreg[0],sf.credreg[5]))
        if list(x)[0][0]==0:
            if sf.credreg[0]=="" or sf.credreg[1]=="" or sf.credreg[2]=="" or sf.credreg[3]=="" or sf.credreg[5]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r)"%(sf.credreg[0],sf.credreg[1],sf.credreg[2],sf.credreg[3],sf.credreg[4],sf.credreg[5]))
                sf.con.commit()
                messagebox.showinfo("Register","You are Successfully Registered")
                sf.Login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")

    def midder_update(sf):
        if(len(sf.cartlist)!=0):
            for h in sf.cartlist:
                    print(f"==={h}===")
                    sf.Qrder_quantity.update({h[1]:sf.Qrder_quantity.get(h[1])+int(h[3])})
                    print(sf.Qrder_quantity.get(h[1]))

            with open("Qrder_quantity.txt", "w", encoding="utf8") as f:
                for k,v in sf.Qrder_quantity.items():
                    f.write(f"{str(k)},{str(v)}" + "\n")
                    print(k,v)

            with open("menu.txt", "a", encoding="utf8") as f:
                for m in sf.cartlist:
                    f.write(str(m) + "\n")
                    # f.write("{}\n".format(m.capitalize()))
            sf.id += 1
        else:
            messagebox.showinfo("","Please select your menu")

    def midder_open(sf):

            os.system('%s %s' % (py,'mid_restaurant.py'))
            # sf.up_load_data_menu()
        
    
    def up_load_data_order(sf):
        f = open("Qrder_quantity.txt")
        for row in f:
            temp_roe = row.split(",")
            sf.Qrder_quantity.update( {str(temp_roe[0]) : int(temp_roe[1])} )
        f.close()
        print(sf.Qrder_quantity)
        

    def test_summary(sf):
        os.system('%s %s' % (py,'Summary.py'))

    def test_receipt(sf):
        os.system('%s %s' % (py,'Receipt.py'))

 
x=LostInDelicious()
x.main()

