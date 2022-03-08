import tkinter as tk
import random

root = tk.Tk()
root.geometry("500x300")
myScL = tk.Label(
    root, 
    text = "I knew it",
    font=("Arial", 25)
)
myLabel = tk.Label(
    root, 
    text= "Are you dumb?",
    font=("Arial", 25)
)

def delete():
    yesButton.destroy()
    noButton.destroy()
    myLabel.destroy()
    myScL.pack()

def Ckicked(event):
    x = random.randint(10,400)
    y = random.randint(70,250)
    noButton.place(x=x, y=y)
    
yesButton = tk.Button(
    text="Yes",
    width=10,
    height=3,
    bg="white",
    fg="black",
    command = delete,
    activebackground='#345',
    activeforeground='white', 
    relief="raised",
)

noButton = tk.Button(
    text="no",
    width=10,
    height=3,
    bg="white",
    fg="black",
    activebackground='#345',
    activeforeground='white',  
    relief="raised",
)

noButton.bind("<Button-1>", Ckicked)
yesButton.place(x=90, y=70)
noButton.place(x=290, y=70)
myLabel.pack()
root.title("Are you smart enough")

root.mainloop()