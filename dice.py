from tkinter import*
import random
window= Tk()
window.title("Dice")
window.geometry("200x200")
options= [0,1,2,3,4,5,6]
def everything():   
    num= random.choice(options)
    number.config(text=str(num))
    if num==6:
        number.config(text=str(num),fg="red")
    elif num !=6:
        number.config(text=str(num),fg="black")

text= Label(window,text="Roll the Dice!",font="Arial 20 bold")
text.place(x=10,y=10)
number= Label(window,text="",font="Arial 50 bold")
number.place(x=75,y=65)
roll= Button(window,text="roll",command=everything ,font="Arial 10 bold")
roll.place(x=87,y=150)
window.mainloop()