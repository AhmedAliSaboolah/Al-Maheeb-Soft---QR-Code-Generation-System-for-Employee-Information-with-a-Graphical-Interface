from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox


#أسم النظام
rot = Tk()
rot.title("المهيب")
rot.geometry("370x515+500+100")
rot.resizable(False,False)


#صوت الترحيب

    
#الأصوات
wel=pyttsx3.init()
voices= wel.getProperty('voices')
wel.setProperty('voice',voices[1].id)

def Speak(audio):
    wel.say(audio)
    wel.runAndWait()


def TakeCommands():
    command= sr.Recognizer()
    with sr.Microphone() as mic:
        command.phrase_threshold=0.1
        audio = command.listen(mic)
        try:
            query = command.recognize_google_cloud(audio , language='ar')
        except Exception as Error:
            print(Error)
        return query.lower()


#برمجة الازرار
def B1 ():
    query = TakeCommands()
    name = query
    E1.insert(0,name)

def B2 ():
    query = TakeCommands()
    name = query
    E2.insert(0,name)

def B3 ():
    query = TakeCommands()
    name = query
    E3.insert(0,name)

def Sv():
    namefile = En_save.get()
    name = E1.get()
    co   = E2.get()
    job  = E3.get()
    info = qrcode.make( name + co + job )
    info.save('employee/'+namefile+'.jpg')
    messagebox.showinfo('Save','Save['+ namefile + ']employee')


#الصورة
photo=PhotoImage(file='44.png')
l_img = Label(rot,image=photo)
l_img.place(x=2, y=1, width=365,height=200)


#النصوص
l=Label(rot, text='Emp Name:',font=('Cairo',14))
l.place(x=10,y=230)

l1=Label(rot, text='Country:',font=('Cairo',14))
l1.place(x=10,y=270)

l2=Label(rot, text='Emp Jop:',font=('Cairo',14))
l2.place(x=10,y=310)


#حقول الأدخال
E1=Entry(rot,font=('Cairo',14))
E1.place(x=130 , y=230)

E2=Entry(rot,font=('Cairo',14))
E2.place(x=130 , y=270)

E3=Entry(rot,font=('Cairo',14))
E3.place(x=130 , y=310)


#الأزرار الجانبية
B1=Button(rot, text='🔊',bg='black', fg='white',font=('Cairo',9),command=B1)
B1.place(x=340, y=230)

B2=Button(rot, text='🔊', bg='black', fg='white',font=('Cairo',9),command=B2)
B2.place(x=340, y=270)

B3=Button(rot, text='🔊', bg='black', fg='white',font=('Cairo',9),command=B3)
B3.place(x=340, y=310)


#الحفظ
l_save= Label(rot, text='File Save :',font=('Cairo',14))
l_save.place(x=10,y=382)
En_save=Entry(rot,font=('Cairo',16),width=11)
En_save.place(x=137,y=380)
b_save=Button(rot , text='Save✅',fg='white',bg='red',font=('Cairo',11), command=Sv )
b_save.place(x=286, y=378)


#حقوق النشر
l_copy=Label(rot, text='المهيب أحمدعلي', font=('Cairo',14))
l_copy.place(x=130, y=435)






rot.mainloop() 