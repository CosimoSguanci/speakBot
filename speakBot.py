#speakBot V0.50
import RPi.GPIO as GPIO
import time
from tkinter import *
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Scrivi lettera/spazio
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)#STICK: lettera -
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP) #STICK: lettera +
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)#Cancella lettera
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP) #TTS
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)#Spegnimento



x=0 #Variabile globale utile a determinare quale lettEra mostrare
s="" #Stringa che serve a concatenare le lettere per  mostrare la parola


class mainGUI:
    def __init__(self, parent):
        self.mioContenitore=Frame(parent)
        self.mioContenitore.pack()

        
        self.schermataSx=Button(self.mioContenitore, height=600, width=330)
        self.schermataSx["background"]="white"
        self.schermataSx.config(font=("helvetica",80))
        self.schermataSx.pack(side=LEFT)
        
        


        self.schermataDx=Label(self.mioContenitore,wraplength=400)
        self.schermataDx["background"]="white"
        self.schermataDx.config(font=("helvetica", 60)) #wraplength da rivedere
        self.schermataDx.config(height=50,width=30,anchor=W)
        self.schermataDx.pack(side=LEFT)


        

    def cambioLett(self):
        global x
        global a
        if(GPIO.input(5)==0):
            time.sleep(0.60) # Ritardo cambio lettera da rivedere
            x+=1
        if(GPIO.input(12)==0):
            x-=1
        if(GPIO.input(7))==0: #TTS: Dice solo la prima parola
            os.system("pico2wave -l it-IT -w speak.wav \""+s+"\" ")
            #os.system("pico2wave -l it-IT -w speak.wav \"Ciao Mamma\" ")
            os.system("aplay speak.wav")

        if(GPIO.input(23))==0:
            os.system("sudo shutdown -h now")
            
        if x==0:
            #self.schermataSx["text"]="A"
            self.backgroundImage = PhotoImage(file="IMG/A.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=5:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        
                
                
    
        if x==1:
            self.backgroundImage = PhotoImage(file="IMG/B.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

           

           
        if x==2:
            self.backgroundImage = PhotoImage(file="IMG/C.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==3:
            self.backgroundImage = PhotoImage(file="IMG/D.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==4:
            self.backgroundImage = PhotoImage(file="IMG/E.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==5:
            self.backgroundImage = PhotoImage(file="IMG/F.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==6:
            self.backgroundImage = PhotoImage(file="IMG/G.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==7:
            self.backgroundImage = PhotoImage(file="IMG/H.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==8:
            self.backgroundImage = PhotoImage(file="IMG/I.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==9:
            self.backgroundImage = PhotoImage(file="IMG/L.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

          
        if x==10:
            self.backgroundImage = PhotoImage(file="IMG/M.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==11:
            self.backgroundImage = PhotoImage(file="IMG/N.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==12:
            self.backgroundImage = PhotoImage(file="IMG/O.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==13:
            self.backgroundImage = PhotoImage(file="IMG/P.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==14:
            self.backgroundImage = PhotoImage(file="IMG/Q.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==15:
            self.backgroundImage = PhotoImage(file="IMG/R.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==16:
            self.backgroundImage = PhotoImage(file="IMG/S.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==17:
            self.backgroundImage = PhotoImage(file="IMG/T.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==18:
            self.backgroundImage = PhotoImage(file="IMG/U.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

        if x==19:
            self.backgroundImage = PhotoImage(file="IMG/V.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==20:
            self.backgroundImage = PhotoImage(file="IMG/Z.png")
            self.schermataSx["image"]=self.backgroundImage
            time.sleep(0.25)
            if(GPIO.input(17)==0):
                time.sleep(0.25)
                cont=0
                while(GPIO.input(17))==0:
                    cont=cont+1
                    time.sleep(0.5)
                if cont>=3:
                    self.scriviSpazio()
                else:
                    self.scriviLett()

            if(GPIO.input(26))==0:
                self.cancellaLett()

            
        if x==21:
            time.sleep(0.25)
            x=0

        if(x==-1):
            time.sleep(0.25)
            x=20

        self.mioContenitore.after(10,self.cambioLett)

    def scriviLett(self):
        global s
        global x
        if(x==0):
            s+="A"
            self.schermataDx["text"]=s
        if(x==1):
            s+="B"
            self.schermataDx["text"]=s
        if(x==2):
            s+="C"
            self.schermataDx["text"]=s
        if(x==3):
            s+="D"
            self.schermataDx["text"]=s
        if(x==4):
            s+="E"
            self.schermataDx["text"]=s
        if(x==5):
            s+="F"
            self.schermataDx["text"]=s
        if(x==6):
            s+="G"
            self.schermataDx["text"]=s
        if(x==7):
            s+="H"
            self.schermataDx["text"]=s
        if(x==8):
            s+="I"
            self.schermataDx["text"]=s
        if(x==9):
            s+="L"
            self.schermataDx["text"]=s
        if(x==10):
            s+="M"
            self.schermataDx["text"]=s
        if(x==11):
            s+="N"
            self.schermataDx["text"]=s
        if(x==12):
            s+="O"
            self.schermataDx["text"]=s
        if(x==13):
            s+="P"
            self.schermataDx["text"]=s
        if(x==14):
            s+="Q"
            self.schermataDx["text"]=s
        if(x==15):
            s+="R"
            self.schermataDx["text"]=s
        if(x==16):
            s+="S"
            self.schermataDx["text"]=s
        if(x==17):
            s+="T"
            self.schermataDx["text"]=s
        if(x==18):
            s+="U"
            self.schermataDx["text"]=s
        if(x==19):
            s+="V"
            self.schermataDx["text"]=s
        if(x==20):
            s+="Z"
            self.schermataDx["text"]=s

    def scriviSpazio(self):
        global x
        global s
        s+=" "
        

    def cancellaLett(self):
        global s
        s=s[:-1]
        self.schermataDx["text"]=s


root=Tk()
root.attributes('-fullscreen',True)
GUI=mainGUI(root)
GUI.cambioLett()
root.mainloop()
