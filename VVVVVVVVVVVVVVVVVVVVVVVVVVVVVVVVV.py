


#A.Singh:


from tkinter import *
from tkinter import ttk,messagebox
from googletrans import Translator,LANGUAGES
import textblob



root=Tk()
root.title("Translator")
root.geometry("1080x740")

#root.iconbitmap("C:/Users/shash/Desktop.ico")

root.resizable(0,0)
root.configure(bg="black")

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
def data():
    s=combo1.get()
    d=combo2.get()
    msg=t1.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    t2.delete(1.0,END)
    t2.insert(END,textget)


        

#languages=googletrans.LANGUAGES
language_list=list(LANGUAGES.values())


def delete():
    t1.delete(1.0,END)
    t2.delete(1.0,END)


        
f1=Frame(root,bg="black",bd=5,relief=SUNKEN)
f1.place(x=30,y=80,width=440,height=210)

t1 = Text(f1, width=30,height=15,borderwidth=5,relief=RIDGE,bg="sky blue")
t1.place(x=0,y=0,width=430,height=200)
t1.insert(1.0,"Enter text to translate......")

combo1=ttk.Combobox(root,value=language_list,font="Roboto",state="r")
combo1.place(x=30,y=50,width=440)
combo1.set('ENGLISH')
   

button=Button(root,text="TRANSLATE",command=data,bg="#00ff00",fg="black",padx=10,pady=5)
button.place(x=490,y=150)

button=Button(root,text="DELETE ALL",command=delete,bg="#00ff00",fg="black",padx=10,pady=5)
button.place(x=490,y=200)

f2=Frame(root,bg="black",bd=5,relief=SUNKEN)
f2.place(x=600,y=80,width=440,height=210)

t2 = Text(f2,width=30,height=15,borderwidth=5,relief=RIDGE,bg='sky blue')
t2.place(x=0,y=0,width=430,height=200)


combo2=ttk.Combobox(root,value=language_list,font="Roboto",state="r")
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





#[8:58 PM, 6/13/2022] A.Singh


from tkinter import *
from tkinter import ttk,messagebox

from googletrans import Translator,LANGUAGES

root=Tk()
root.title("Translator")
root.geometry("1080x740")



root.resizable(0,0)
root.configure(bg="black")
#def Translate():
    #translator = Translator()
    #translated=translator.translate(text= text1.get(1.0, END) , src = combo1.get(), dest =combo2.get())
    #text2.delete(1.0, END)
    #text2.insert(END, translated.text)


def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
def data():
    s=combo1.get()
    d=combo2.get()
    msg=t1.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    t2.delete(1.0,END)
    t2.insert(END,textget)


languageS=list(LANGUAGES.values())


def delete():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    


f1=Frame(root,bg="black",bd=5,relief=SUNKEN)
f1.place(x=30,y=80,width=440,height=210)


text1 = Text(f1, width=30,height=15,borderwidth=5,relief=RIDGE,bg="sky blue")
text1.place(x=0,y=0,width=430,height=200)
text1.insert(1.0,"Enter text to translate......")

combo1=ttk.Combobox(root,value=languageS,font="Roboto",state="r")
combo1.place(x=30,y=50,width=440)
combo1.set('ENGLISH')

f2=Frame(root,bg="black",bd=5,relief=SUNKEN)
f2.place(x=600,y=80,width=440,height=210)        



text2 = Text(f2,width=30,height=15,borderwidth=5,relief=RIDGE,bg='sky blue')
text2.place(x=0,y=0,width=430,height=200)



combo2=ttk.Combobox(root,values=languageS,font="Roboto",state="r")
combo2.place(x=600,y=50,width=438)
combo2.set("CHOOSE LANGUAGE")


scroll1=Scrollbar(text1)
scroll1.pack(side="right",fill="y")
scroll1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll1.set)



scroll2=Scrollbar(text2)
scroll2.pack(side="right",fill="y")
scroll2.configure(command=text2.yview)
text2.configure(yscrollcommand=scroll2.set)

button=Button(root,text="TRANSLATE",command=data,bg="#00ff00",fg="black",padx=10,pady=5)
button.place(x=490,y=150)



button=Button(root,text="DELETE ALL",command=delete,bg="#00ff00",fg="black",padx=10,pady=5)
button.place(x=490,y=200)

#quit=Button(root,text="EXIT",command=root.quit).pack()





root.mainloop()






