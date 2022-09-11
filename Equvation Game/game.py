import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time Counter")


second = StringVar()
second.set("00")
secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def submit():
    temp = 5
    while temp > -1:
        secs = temp % 60
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp -= 1

btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit)
btn.place(x=70, y=120)
root.mainloop()
