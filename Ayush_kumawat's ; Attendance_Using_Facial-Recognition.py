import face_recognition
import cv2
import os
import pandas as pd
from datetime import datetime
import time
from tkinter import *

lis=[]

# Insert Location of excel file saved
face_cascade = cv2.CascadeClassifier(r'C:\Users\hp\OneDrive\Desktop\recr\face_dectect.xml')
na=""

count=0

def name():
     
    root = Tk()
    root.title("Credintials Login")
    root.geometry("500x280")
    root.geometry()

    root.minsize(200, 200)

    # Set maximum window size value
    
    root.maxsize(500, 200)
    c=Canvas(root,bg="gray16",height=200,width=200)
    filename=PhotoImage(file=r"C:\Users\hp\Downloads\fw-bg-gradient.png")
    background_lable=Label(root,image=filename)
    background_lable.place(x=0,y=0)
                          

    label=Label(root,font=('Times New Roman',23),text='Entre Username & Password',borderwidth=0,relief="flat",bg="#4FB576")
    label.pack()
    username = "abc" #that's the given username
    password = "cba" #that's the given password

    # Username entry
    user_name = Label(root,font=('Calibri Body',11),text = "Username:",bg="#4FB576").place(x = 65,y = 42)
    username_entry = Entry(root,width = 35)
    username_entry.pack()


    # Password entry
    user_password = Label(root,font=('Calibri Body',11,),text = "Password:",bg="#4FB576").place(x = 65,y = 60)
                              
    password_entry = Entry(root, show='*',width=35)
    password_entry.pack()

    def trylogin():
        global na
        global count      
        """This method is called when the button is pressed
            to get what's written inside the entries, I used get()
            check if both username and password in the entries are same of the given ones"""
        # Insert Location of excel file saved      
        df1=pd.read_excel(r"C:\Users\hp\OneDrive\Desktop\recr\Bookss.xlsx")
        if username_entry.get()=="":
            label1.config(text="plz enter your name")
        elif username_entry.get().capitalize() in list(df1.professor):
            label1.config(text="name already present")
            password_entry.delete(0,END)
        elif password == password_entry.get():
            print("Correct")
            na=username_entry.get()
            if na not in list(df1.professor):
               new={"professor":na.capitalize()}
               print("lll")
               df1=df1.append(new,ignore_index=True)
               df1.to_excel(r"C:\Users\hp\OneDrive\Desktop\recr\Bookss.xlsx",index=False)
               print(df1)
        else:
            print("Wrong")
            na=""
            label1.config(text="inncorrect password")
            password_entry.delete(0,END)
            count+=1
            if count==3:
                root.destroy()
        return na
    label1=Label(root,font=('helvetica',10,),text="",bg="#4FB576",borderwidth=0)
    label1.pack()
    
    #When you press this button, trylogin is called
    button = Button(root,font=('Times New Roman',15,'bold'),text="Submit",bg="#4FB576", command = trylogin)
    button.pack()
    
    label=Label(root,font=('helvetica',7,),text='Creidentials Login Details!',bg="#4FB576")
    #Label.config(bg='GREEN')
    label.pack()
    #App starter
    root.mainloop()

def update():
    global na
    print(na)
    lis=[]
    z=[]
    g=0
    face_cascade = cv2.CascadeClassifier(r'C:\Users\hp\OneDrive\Desktop\recr\face_dectect.xml')
    cap = cv2.VideoCapture(1)
    
    while True:
        _, frame = cap.read()
        frame=cv2.flip(frame,1)
        image=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        f=cv2.waitKey(1)
        if f%256 == 32 or g!=0:
                g=1
                if len(lis)==0: # This condition is given to excute code only once
                            # Making timer of 6 seconds
                            lis.append(1)
                            z=[]
                            n=1
                            print("ll") 
                if len(lis)!=0: # For displaying 5 second timer on screen without freezing frame
                    cv2.putText(frame,str(n),(50,50),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,0),2)
                    k=datetime.now().strftime("%S")[-1]
                    if len(z)==0:
                        z.append(k)
                    if z[0]!=k:
                        z=[]
                        n+=1
                    if n==6:
                        try:
                            # for face dectection so that you can take croped image of your face
                            for x, y, w, h in face:
                                face_roi = frame[y-80:y+h+80, x-80:x+w+80]
                            cv2.imwrite(r"C:\Users\hp\OneDrive\Desktop\source code\images\\"+na.capitalize()+".png",face_roi)
                            break
                        except:        
                                lis=[]
                                print("try again")
                                g=0
                                pass
        cv2.imshow('cam star', frame)
        try:
           if cv2.waitKey(10) == ord('q'):
                break
        except:
            print("pp")
            pass
    cap.release()
    cv2.destroyAllWindows()

def facee():

    global m
    df=pd.read_excel(r"C:\Users\hp\OneDrive\Desktop\recr\Bookss.xlsx")
    video=cv2.VideoCapture(1)
    video.set(cv2.CAP_PROP_BUFFERSIZE,1)
    path=r"C:\Users\hp\OneDrive\Desktop\source code\images"
    photo=[r"C:\Users\hp\OneDrive\Desktop\source code\images"+"\\"+i for i in os.listdir(path)]
    known_face_encod=[face_recognition.face_encodings(face_recognition.load_image_file(i))[0] for i in photo]
    known_face_name=[i[:i.index(".")] for i in os.listdir(path)]
    unknown=""
    
    while True:
        try:
            ret,frame=video.read()
            frame=cv2.flip(frame,1)
            frame_copy=frame.copy()
            ha=frame.copy()
            frame=cv2.resize(frame,(0,0),fx=0.20,fy=0.20)
            
            ha=cv2.resize(ha,(0,0),fx=0.50,fy=0.50)
            gray = cv2.cvtColor(ha, cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(gray, 1.3, 5)
                                
            rgb_frame=frame[:,:,::-1]
            
            img1_loc=face_recognition.face_locations(rgb_frame)
            img1_encod=face_recognition.face_encodings(rgb_frame,img1_loc)
            
            if len(img1_encod)==0:
               unknown=""
        except: pass
        for x, y, w, h in face:
                   
                cv2.rectangle(ha,(x,y),(x+w,y+h),(255,255,0),2)
                for (top,right,bottom,left), face_encoding in zip(img1_loc,img1_encod):
                    match=face_recognition.compare_faces(known_face_encod,face_encoding)
                    
#Emotion dectection
                   
                    name="Unknown"
                    if True in match:
                        index=match.index(True)
                        name=known_face_name[index]
                        
                        if name!="Unknown":
                            try:
                                df.loc[list(df.professor).index(name),datetime.now().strftime("%d-%m-20%y").zfill(10)]="y"
                                lis.append(name)
                            except:pass
                    # Updating unknown person's name in attendence sheet
                    if name=="Unknown":
                       print("niu")
                       cv2.putText(ha,"To Update Press: U",(0,40),cv2.FONT_HERSHEY_DUPLEX,0.75,(0,0,0),2)
                       if cv2.waitKey(10) == ord('u'):
                           upda="yes"                               
                    unknown="1"
                    
                    cv2.putText(ha,"Name: "+name,(0,20),cv2.FONT_HERSHEY_DUPLEX,0.75,(0,0,0),2)                    
                    print(name)
        cv2.imshow("hh",ha)
        try:
            if cv2.waitKey(10) == ord('q'):
              m="break"  
              break
            if upda=="yes":
                break
        except:
            pass
    video.release()
    cv2.destroyAllWindows()
    df.to_excel(r"C:\Users\hp\OneDrive\Desktop\recr\Bookss.xlsx",index=False)
    
while True:
    facee()
    try:
      if m=="break":
        break
    except:
        name()
        print(na)
        if na=="":
            continue
        update()