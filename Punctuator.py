#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *

window=Tk()


frame=Frame(window,bg="#8CC0DE")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

def clear_text():
   t1.delete("1.0", "end")
   e1.delete(0,END)


def sentence_maker():
    phrase=e1_value.get()
    temp=[]
    questions=("how","why","what","when","where","is")
    greetings=("hi","hello","hey")
    parts=phrase.split(" ")
    for words in parts:
        if words!="i":
            temp.append(words)
        else:
            temp.append(words.capitalize())
    parts=" ".join(temp)
    capitalized=parts.capitalize()
    if phrase.startswith(questions):
        result="{}? ".format(capitalized)
        t1.insert(END,result)
        
    elif phrase.startswith(greetings):
        result="{}! ".format(capitalized)  
        t1.insert(END,result)    
    else:
        result= "{}. ".format(capitalized)
        t1.insert(END,result)


l1=Label(window,text="Hi there! Let me do some simple punctuation to your text. Enter the text in the first box and click on execute.",font=("Calibri 20"),bg="white")
l1.place(x=180,y=120)

b1=Button(window,text="Execute",command=sentence_maker,bg="white")
b1.place(relwidth=0.05,relheight=0.05,relx=0.4,rely=0.8)

b2=Button(window,text="Clear",command=clear_text,bg="white")
b2.place(relwidth=0.05,relheight=0.05,relx=0.55,rely=0.8)


e1_value=StringVar()
e1=Entry(window,textvariable=e1_value,font=("Calibri 16"))
e1.place(height=60,width=400,relx=0.37,rely=0.3)

t1=Text(window,height=7,width=20,font=("Calibri 16"))
t1.place(height=200,width=400,relx=0.37,rely=0.5)

window.mainloop()


# In[ ]:




