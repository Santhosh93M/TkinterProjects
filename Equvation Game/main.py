import time
from tkinter import *
from tkinter import messagebox
from random import choice, randint

high_score = 0
count = 0


class Application(object):

    def __init__(self, master):
        self.master = master

        # Frames
        mainFrame = Frame(self.master)
        mainFrame.pack()
        self.top = Frame(mainFrame, width=300, height=400, bg='white', borderwidth=10)
        self.top.pack(side=LEFT, fill=Y)
        self.bottom = Frame(mainFrame, width=400, height=400, bg="skyblue", borderwidth=2)
        self.bottom.pack()

        # Headings, Images and Date
        self.top_image = PhotoImage(file="icons/game.png")
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=100, y=75)
        self.heading = Label(self.top, text="Equation Solving", fg='blue', bg='white', font="Times 18 bold")
        self.heading.place(x=65, y=180)

        # start game button
        self.game_icon = PhotoImage(file="icons/member.png")
        self.game_btn = Button(self.bottom, width=15, text="Start Game", font="Times 12 bold", bg='pink',
                               command=self.start_fun)
        # self.person_btn.config(image=self.per_icon, compound=LEFT, width=5, height=10)
        self.game_btn.place(x=80, y=100)

        # high score button
        self.add_btn = Button(self.bottom, width=15, text="High Score", font="Times 12 bold", bg='pink',
                              command=self.score_fun)
        self.add_btn.place(x=80, y=140)

        # exit button
        self.exit_btn = Button(self.bottom, width=15, text="Exit", font="Times 12 bold", bg='pink',
                               command=self.exit_fun)
        self.exit_btn.place(x=80, y=180)

    def start_fun(self):
        app = StartGame()
        app.change_values()

    def score_fun(self):
        score = Score()

    def exit_fun(self):
        self.master.destroy()


class StartGame(Toplevel):
    global count
    global high_score

    def __init__(self):

        Toplevel.__init__(self)
        self.geometry("450x500+600+100")
        self.title("Game")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white', relief=SUNKEN)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=410, bg="pink")
        self.bottom.pack(fill=X)

        # Display
        self.display_entry = Entry(self.top, width=20, font="Times 12 bold", bd=5)
        self.display_entry.insert(0, "16 + 14 = ?")
        self.display_entry.place(x=150, y=60)

        # countdown
        self.second = StringVar()
        self.second.set("00")
        self.count_entry = Entry(self.top, width=5, textvariable=self.second, font="Times 12 bold", bd=5, justify=RIGHT)
        self.count_entry.place(x=330, y=5)

        # labels
        self.entry_lbl = Label(self.top, text="Find :", fg='black', bg='white', font='Times 15 bold')
        self.entry_lbl.place(x=90, y=57)

        self.ct_lbl = Label(self.top, text="countdown : ", fg='red', bg='white', font='Times 12 bold')
        self.ct_lbl.place(x=250, y=5)

        self.res_lbl = Label(self.bottom, text=f"your score is : 0", fg='red', bg='white', font='Times 15 bold')
        self.res_lbl.place(x=120, y=200)

        # Buttons
        self.no1_btn = Button(self.bottom, width=10, text="30", font='Times 12 bold', bg='lightgreen',
                              command=self.btn_1)
        self.no1_btn.place(x=80, y=40)

        self.no2_btn = Button(self.bottom, width=10, text="50", font='Times 12 bold', bg='lightgreen',
                              command=self.btn_2)
        self.no2_btn.place(x=230, y=40)

        self.no3_btn = Button(self.bottom, width=10, text="09", font='Times 12 bold', bg='lightgreen',
                              command=self.btn_3)
        self.no3_btn.place(x=80, y=100)

        self.no4_btn = Button(self.bottom, width=10, text="20", font='Times 12 bold', bg='lightgreen',
                              command=self.btn_4)
        self.no4_btn.place(x=230, y=100)
        self.countdown()

    def btn_1(self):
        self.check_ans(int(self.no1_btn['text']))

    def btn_2(self):
        self.check_ans(int(self.no2_btn['text']))

    def btn_3(self):
        self.check_ans(int(self.no3_btn['text']))

    def btn_4(self):
        self.check_ans(int(self.no4_btn['text']))

    # for countdown , if countdown stopped the game will end
    def countdown(self, temp=60):
        while temp > -1:
            self.second.set(f"{temp}")
            self.update()
            time.sleep(1)
            if temp == 0:
                messagebox.showinfo("Time's up", f"{self.res_lbl['text']}")
                self.destroy()
                break
            temp -= 1

    # check the values if It's correct or not
    def check_ans(self, value):
        global high_score, count
        if value == int(eval(self.display_entry.get().split("=")[0])):
            count += 1
            print("success")
            self.res_lbl.config(text=f"Your score is: {count}")
            if count > high_score:
                high_score = count
            # self.count_down(StartGame.count)
        self.change_values()
            # self.countdown()
        # else:
            # messagebox.showinfo("Game over", str(self.res_lbl['text']), icon="info")
            # self.destroy()

    # if the ans is correct this method used to change the equation
    def change_values(self):
        self.display_entry.delete(0, END)
        operation = ["+", "-", "*", "/", "%"]
        self.display_entry.insert(0, f"{str(randint(1, 100))} {choice(operation)} {str(randint(1, 100))} = ?")

        buttons_value = [self.no1_btn, self.no2_btn, self.no3_btn, self.no4_btn]
        ans_btn = choice(buttons_value)
        for btn in buttons_value:
            if btn == ans_btn:
                btn['text'] = str(int(eval((self.display_entry.get().split("=")[0]))))
            else:
                btn['text'] = str(randint(0, 100))


class Score(Toplevel):
    global high_score

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("300x150+700+150")
        self.title("High Score")
        self.resizable(False, False)

        # label , for show the high score obtained by user
        score_lbl = Label(self, text="High Score is: "+str(high_score), font="Times 15 bold")
        score_lbl.place(x=80, y=55)


def main():
    root = Tk()
    app = Application(root)
    root.title("Equation Game")
    root.geometry("600x400+600+100")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
