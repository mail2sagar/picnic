from tkinter import *
import random
window = Tk()

window.title("Picnic Bag List")
window.geometry("500x500")

label1 = Label(window)
label2 = Label(window)

list1 = ["bottle","food","mat","containers"]

def list_things():
    random_th = random.randint(0,3)
    label1["text"]="Put Item Number "+str(random_th)+" in the Bag"

btn = Button(window,text="What Item to Put in the Bag?",command=list_things)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)


window.mainloop()