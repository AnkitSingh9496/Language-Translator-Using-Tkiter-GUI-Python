# Language-Translator-Using-Tkiter-GUI-Python
#PROGRAM ****************************************************************************************************
#************************************************************************************************************************
#*******************************************************************************************************************************


from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob

#def newwindow():
	#new_window=Tk()

root=Tk()
root.title("Translator")
root.geometry("1080x740")

#root.iconbitmap("C:/Users/shash/Desktop.ico")

root.resizable(0,0)
root.configure(bg="black")



def trans():
    #global languages
    #global language_s
    t2.delete(1.0,END)
    try:
        for key,value in languages.items():
            if(value==combo1.get()):
                from_languages_key=key
        for key,value in languages.items():
            if(value==combo2.get()):
                to_languages_key=key
        text=textblob.TextBlob(t1.get(1.0,END))
        text=text.translate(from_lang=from_languages_key,to=to_languages_key)
        t2.insert(1.0,text)
        #text=text.translate(from_=t1,to=t2)
    except Exception as e:
        messagebox.showerror("Translator",e)
        

languages=googletrans.LANGUAGES
language_s=list(languages.values())




#languages=googletrans.LANGUAGES
#language_s=list(languages.values())
#print(language_s)

def delete():
    t1.delete(1.0,END)
    t2.delete(1.0,END)
    

#photo=PhotoImage(file="C:\\Users\\shash\\Desktop\\google-translate-logo-emblem-symbol-services-application-12")
#label=Label(root,text="hello",image=photo)

#print(language_s)

        




f1=Frame(root,bg="black",bd=5,relief=SUNKEN)
f1.place(x=30,y=80,width=440,height=210)

t1 = Text(f1, width=30,height=15,borderwidth=5,relief=RIDGE,bg="sky blue")
t1.place(x=0,y=0,width=430,height=200)
t1.insert(1.0,"Enter text to translate......")

combo1=ttk.Combobox(root,value=language_s,font="Roboto",state="r")
combo1.place(x=30,y=50,width=440)
combo1.set('ENGLISH')
   

button=Button(root,text="TRANSLATE",command=trans,bg="#00ff00",fg="black",padx=10,pady=5)
button.place(x=490,y=150)

button=Button(root,text="DELETE ALL",command=delete,bg="#00ff00",fg="black",padx=10,pady=5)
button.place(x=490,y=200)

f2=Frame(root,bg="black",bd=5,relief=SUNKEN)
f2.place(x=600,y=80,width=440,height=210)

t2 = Text(f2,width=30,height=15,borderwidth=5,relief=RIDGE,bg='sky blue')
t2.place(x=0,y=0,width=430,height=200)


combo2=ttk.Combobox(root,value=language_s,font="Roboto",state="r")
combo2.place(x=600,y=50,width=438)
combo2.set("CHOOSE LANGUAGE")

scroll1=Scrollbar(t1)
scroll1.pack(side="right",fill="y")
scroll1.configure(command=t1.yview)
t1.configure(yscrollcommand=scroll1.set)






quit=Button(root,text="EXIT",command=root.quit).pack()



scroll2=Scrollbar(t2)
scroll2.pack(side="right",fill="y")
scroll2.configure(command=t2.yview)
t2.configure(yscrollcommand=scroll2.set)

root.mainloop()
