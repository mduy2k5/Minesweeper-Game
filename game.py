#Import necessary libary 
import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image
import customtkinter  #type : ignore
from tkinter import ttk
from data import *
import random
import time
import os

#Read file function
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Set theme and default game level
level = 4
customtkinter.set_default_color_theme("dark-blue")

#Main code
class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #Create app window
        self.geometry("402x771")
        self.title("Minesweeper")
        self.configure(fg_color="#181a1b")
        self.iconbitmap(resource_path("icon.ico"))

        #Startframe
        self.startframe = customtkinter.CTkFrame(self,corner_radius=0)
        self.startframe.pack(fill='both', expand=True)  

        img_start = ImageTk.PhotoImage(Image.open(resource_path("start.png"))) # type: ignore
        
        self.winlabel = customtkinter.CTkLabel(self.startframe,image = img_start,text="",text_color='#181a1b')
        self.winlabel.place(x=75,y=280)
        
        self.startbutton = customtkinter.CTkButton(self.startframe,corner_radius=20,height=40,width=230,text='Start',hover_color="#84eeab",fg_color="#A1EEBD",text_color='white',command=self.level_select)
        self.startbutton.place(x=85,y=335)
        
        
        self.winlabel1 = customtkinter.CTkLabel(self.startframe,text="Quy tắc quét mìn rất đơn giản. Bàn cờ được chia thành các ",text_color='White')
        self.winlabel1.place(x=32,y=400)
        self.winlabel2 = customtkinter.CTkLabel(self.startframe,text="ô, với các quả mìn được phân bố ngẫu nhiên. Để giành ",text_color='White')
        self.winlabel2.place(x=32,y=422)
        self.winlabel3 = customtkinter.CTkLabel(self.startframe,text="chiến thắng, bạn cần mở tất cả các ô. Con số trên một ô ",text_color='White')
        self.winlabel3.place(x=32,y=444)
        self.winlabel2 = customtkinter.CTkLabel(self.startframe,text="hiển thị số lượng mỏ liền kề với nó. Sử dụng thông tin này, ",text_color='White')
        self.winlabel2.place(x=32,y=466)
        self.winlabel2 = customtkinter.CTkLabel(self.startframe,text="bạn có thể xác định các ô an toàn và các ô có chứa mìn.",text_color='White')
        self.winlabel2.place(x=32,y=488)
        self.winlabel2 = customtkinter.CTkLabel(self.startframe,text="Các ô bị nghi ngờ là của mìn có thể được đánh dấu bằng ",text_color='White')
        self.winlabel2.place(x=32,y=510)
        self.winlabel2 = customtkinter.CTkLabel(self.startframe,text="cờ bằng nút chuột phải.",text_color='White')
        self.winlabel2.place(x=32,y=532)
        self.mainloop()

    #Game code   
    def game(self):
        try: self.level_slt.destroy()
        except: pass
        alre = []
        files = [] 
        btn = [] 
        labl = []
        bom = [] 

        #Function action when click at zero 
        def click_zero(i):
            if i not in alre: alre.append(i)
            global score
            
            try: 
                btn[i].destroy()
                
                score += bom[i]
            except: pass
            arr = []
            
            if i -11 >= 0 and (i -11) % 10 != 9 :
                if bom[i -11] == 0: arr.append(i -11)
                try: 
                    btn[i -11].destroy()
                    
                    score += bom[i -11]
                except: pass
            if i -10 >= 0 :
                if bom[i -10] == 0: arr.append(i -10)
                try:  
                    btn[i -10].destroy()
                    
                    score += bom[i -10]
                except: pass
            if i -9 >= 0 and (i -9) %10 != 0 :
                if bom[i -9] == 0: arr.append(i -9)
                try:  
                    btn[i -9].destroy()
                    
                    score += bom[i -9]
                except: pass
            if i -1 >= 0 and (i -1) % 10 != 9 :
                if bom[i -1] == 0: arr.append(i -1)
                try:  
                    btn[i -1].destroy()
                    
                    score += bom[i -1]
                except: pass
            if i +1 < 170 and (i+1) %10 != 0 :
                if bom[i +1] == 0: arr.append(i +1)
                try:  
                    btn[i +1].destroy()
                    
                    score += bom[i +1]
                except: pass

            if i + 9 <170 and (i + 9) %10 != 9 :
                if bom[i + 9] == 0: arr.append(i + 9)
                try:  
                    btn[i + 9].destroy()
                    
                    score += bom[i + 9]
                except: pass
            if i + 10 <170 : 
                if bom[i + 10] == 0: arr.append(i + 10)
                try:  
                    btn[i + 10].destroy()
                    
                    score += bom[i + 10]
                except: pass
            if i + 11 < 170 and (i + 11) %10 != 0 : 
                if bom[i + 11] == 0:  arr.append(i + 11)
                try:  
                    btn[i + 11].destroy()
                    score += bom[i]
                except: pass
            
            for a in arr:
                if a not in alre: 
                    try:click_zero(a)
                    except: pass
                    alre.append(a)
        
        #Set red flag at boom
        def right_click(event):
            global bomre
            
            if event.widget['state'] != tk.DISABLED:
                event.widget.configure(background="#BF3131",state="disabled")
                bomre -= 1
                
            else : 
                event.widget.configure(background="#b2afaf",state=NORMAL)
                bomre += 1
                
            
            
        #Open the bomb hiding place
        def left_click(i):
            if bom[i] == 0:
                click_zero(i)
                if i not in alre: alre.append(i)
  
            else: btn[i].destroy()
                
            dem = 0
            for a in btn:
                if a.winfo_exists(): dem+= 1

            #Calculate score and bom remain
            global score
            global boms
            
            score += bom[i]
            self.bomremain.destroy()
            self.score.destroy()
            self.show()
            #Check if wim
            if dem == boms: self.win(score)
        
        #Create mainframe
        try:self.startbutton.destroy()
        except:pass
        try:self.restartframe.destroy()
        except:pass
        try:self.startframe.destroy()
        except:pass
        try:self.winframe.destroy()
        except:pass
        self.mainframe = customtkinter.CTkFrame(self,corner_radius=0,fg_color="#181a1b")
        self.mainframe.pack(fill='both', expand=True)
        
        

        #Make bom
        global bomre
        bomre = 0
        global score
        score = 0
        for i in range(170): 
            dem = random.randint(level,9)
            bom.append(dem)
            if dem == 9: bomre += 1
        global boms
        boms = bomre
        self.show()

        #Calculate the number show how many boom near it
        for i in range(170):
            if bom[i] != 9:
                count = 0
                if i-11 >= 0 and (i-11) % 10 != 9 :
                    if bom[i-11] == 9: count +=1
                if i-10 >= 0 :
                    if bom[i-10] == 9: count += 1
                if i-9 >= 0 and (i-9) %10 != 0 :
                    if bom[i-9] ==9: count += 1
                if i-1 >= 0 and (i-1) % 10 != 9 :
                    if bom[i-1] == 9: count +=1 
                if i+1 < 170 and (i+1) %10 != 0 :
                    if bom[i+1] ==9: count += 1
                if i+9 <170 and (i+9) %10 != 9 :
                    if bom[i+9] == 9: count += 1
                if i+10 <170 :
                    if bom[i+10] == 9: count += 1
                if i+11 < 170 and (i+11) %10 != 0 :
                    if bom[i+11] == 9: count += 1
                bom[i] = count
                
        for i in range(170): files.append(str(i))

        #create list of number of boom and button hide the boom
        r = 0
        a = 0
        for i in range(len(files)):
            labl.append(tk.Label(self.mainframe,background="#181a1b", text=str(bom[i]),width=4,height=2,fg='white'))
            labl[i].place(x = 10+50*a , y =70+ 53*r,anchor = 'nw')
            a += 1
            if a== 10:
                a =0
                r += 1
        r = 0
        a = 0
        for i in range(len(files)):
            btn.append(tk.Button(self.mainframe,width=6,height=3 ,background="#b2afaf",command= lambda c=i: self.restart(score) if (bom[c] == 9)  else left_click(c) ))
            
            btn[i].bind("<Button-3>",right_click)
            btn[i].place(x = 50*a , y =60+  53*r,anchor = 'nw')
            a += 1
            if a== 10:
                a =0
                r += 1

        
    #show the score amd boom remain
    def show(self):
        self.bomremain = customtkinter.CTkLabel(self.mainframe,text='Bomremain: '+str(bomre),fg_color="#BF3131",corner_radius= 40)     
        self.bomremain.grid(row=0,column=0,padx=50,pady=10)

        self.score = customtkinter.CTkLabel(self.mainframe,text='Score: '+str(score),fg_color="#4CB9E7",corner_radius= 40)     
        self.score.grid(row=0,column=2,padx=50,pady=10)
    
    #Level select function
    def level_select(self):
        global level
        def run(n):
            global level
            level = n
            self.game()
        try:self.startframe.destroy()
        except: pass
        try:self.restartframe.destroy()
        except: pass
        try:self.winframe.destroy()
        except: pass
        self.level_slt =  customtkinter.CTkFrame(self,corner_radius=0,fg_color="#181a1b")
        self.level_slt.pack(fill='both', expand=True)
        self.winlabel = customtkinter.CTkLabel(self.level_slt,text="Start with:",text_color='White')
        self.winlabel.place(x=175,y=290)
        self.startbutton_beginner = customtkinter.CTkButton(self.level_slt,corner_radius=20,height=30,width=230,text='Beginner',hover_color="#84eeab",fg_color="#A1EEBD",text_color='white',command=lambda:run(1))
        self.startbutton_beginner.place(x=85,y=320)
        
        self.startbutton_intermediate = customtkinter.CTkButton(self.level_slt,corner_radius=20,height=30,width=230,text='Intermediate',hover_color="#00a5ea",fg_color="#4CB9E7",text_color='white',command=lambda:run(4))
        self.startbutton_intermediate.place(x=85,y=360)
        
        self.startbutton_expert = customtkinter.CTkButton(self.level_slt,corner_radius=20,height=30,width=230,text='Expert',hover_color="#c31111",fg_color="#BF3131",text_color='white',command=lambda:run(7))
        self.startbutton_expert.place(x=85,y=400)
    
    #Win function
    def win(self,a):
        try:self.mainframe.destroy()
        except: pass
        try:self.bomremain.destroy()
        except: pass
        try:self.score.destroy()
        except: pass
        try:self.startframe.destroy()
        except: pass

        self.winframe = customtkinter.CTkFrame(self,corner_radius=0,fg_color="#181a1b")
        self.winframe.pack(fill='both', expand=True)

        img_win = ImageTk.PhotoImage(Image.open(resource_path("win.png")))

        self.winlabel = customtkinter.CTkLabel(self.winframe,image = img_win,text="",text_color='#212121')
        self.winlabel.place(x=50,y=160)
        self.score = customtkinter.CTkLabel(self.winframe,text="Your score: " + str(a))
        self.score.place(x=160,y=240)
        second = time.time()
        locals = time.localtime(second)
        self.time = customtkinter.CTkLabel(self.winframe,text="Time: " + str(locals.tm_mday) +"/" +str(locals.tm_mon) +"/"+str(locals.tm_year) +"    " + str(locals.tm_hour) +":"+str(locals.tm_min))
        self.time.place(x=145,y=260)

        self.restartbutton = customtkinter.CTkButton(self.winframe,corner_radius=20,height=30,width=230, text='Restart',hover_color="#00a5ea",fg_color="#4CB9E7",text_color='white',command=self.game)
        self.restartbutton.place(x=85,y=290)
        save(str(locals.tm_mday) +"/" +str(locals.tm_mon) +"/"+str(locals.tm_year) +" " + str(locals.tm_hour) +":"+str(locals.tm_min)+"  - "+str(a))

        self.score_label = customtkinter.CTkLabel(self.winframe,text="High score",fg_color="#212121", width=4,height=2,text_color='white')
        self.score_label.place(x=170,y=324)

        col=('top', 'date', 'score')
        self.tree = ttk.Treeview(self.winframe,columns=col,show='headings',height=10)
        self.tree.column('#0', width=0, stretch='no')
        self.tree.heading('top',text="Top")
        self.tree.heading('date',text="Date")
        self.tree.heading('score',text="Score")
        self.tree.column('top', anchor='center', width=50)
        self.tree.column('date', anchor='center', width=190)
        self.tree.column('score', anchor='center', width=100)
        self.tree.place(x = 80,y = 430)
        sv = read()
        for i in sv:
            text = i.split('-')
            self.tree.insert('','end',values=text)
    #Restart function
    def restart(self,score):
        
        try:
            self.mainframe.destroy()
        except:
            pass
        

        self.restartframe = customtkinter.CTkFrame(self,corner_radius=0,fg_color="#181a1b")
        self.restartframe.pack(fill='both', expand=True)
        img_gameover = ImageTk.PhotoImage(Image.open(resource_path("gameover.png")))

        self.loselabel = customtkinter.CTkLabel(self.restartframe,image = img_gameover,text="",text_color='#212121')
        self.loselabel.place(x=52,y=160)
        self.score = customtkinter.CTkLabel(self.restartframe,text="Your score: " + str(score))
        self.score.place(x=160,y=200)
        second = time.time()
        locals = time.localtime(second)
        self.time = customtkinter.CTkLabel(self.restartframe,text="Time: " + str(locals.tm_mday) +"/" +str(locals.tm_mon) +"/"+str(locals.tm_year) +"    " + str(locals.tm_hour) +":"+str(locals.tm_min))
        self.time.place(x=145,y=220)
        

        self.restartbutton = customtkinter.CTkButton(self.restartframe,corner_radius=20,height=30,width=230, text='Restart',hover_color="#00a5ea",fg_color="#4CB9E7",text_color='white',command=self.game)
        self.restartbutton.place(x=85,y=250)
        save(str(locals.tm_mday) +"/" +str(locals.tm_mon) +"/"+str(locals.tm_year) +" " + str(locals.tm_hour) +":"+str(locals.tm_min)+"  - "+str(score))
        
        self.levl = customtkinter.CTkButton(self.restartframe,corner_radius=20,height=30,width=230,text='Level Select',hover_color="#84eeab",fg_color="#A1EEBD",text_color='white',command=self.level_select)
        self.levl.place(x=85,y=290)

        self.score_label = customtkinter.CTkLabel(self.restartframe,text="High score",fg_color="#212121", width=4,height=2,text_color='white')
        self.score_label.place(x=170,y=324)

        col=('top', 'date', 'score')
        self.tree = ttk.Treeview(self.restartframe,columns=col,show='headings',height=10)
        self.tree.column('#0', width=0, stretch='no')
        self.tree.heading('top',text="Top")
        self.tree.heading('date',text="Date")
        self.tree.heading('score',text="Score")
        self.tree.column('top', anchor='center', width=50)
        self.tree.column('date', anchor='center', width=190)
        self.tree.column('score', anchor='center', width=100)
        self.tree.place(x = 78,y = 430)
        sv = read()
        for i in sv:
            #self.list.insert('end', i)
            text = i.split('-')
            self.tree.insert('','end',values=text)

if __name__ == "__main__":
    app()