from tkinter import *
from datetime import datetime
import mypeople, addPeople

date = datetime.now().date()


class Application(object):

    def __init__(self, master):
        self.master = master

        # Frames
        self.top = Frame(master, height=150, bg='white', relief=SUNKEN)
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=400, bg="skyblue")
        self.bottom.pack(fill=X)

        # Headings, Images and Date
        self.top_image = PhotoImage(file=r"C:\Users\elcot\PycharmProjects\TkinterProjects\AddressBook\icons\book.png")
        self.top_image_lbl = Label(self.top, width=150, height=100, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=50, y=15)
        self.heading = Label(self.top, text="My Address Book", fg='blue', bg='white', font="Times 15 bold")
        self.heading.place(x=230, y=50)
        self.date = Label(self.top, text="Today's Date: " + str(date), fg='red', bg='white', font="Times 10 bold")
        self.date.place(x=300, y=5)
        # Person Buttons
        self.per_icon = PhotoImage(file=r"C:\\Users\elcot\PycharmProjects\TkinterProjects\AddressBook\icons\book.png")
        self.person_btn = Button(self.bottom, width=15, text="My People", font="Times 12 bold", bg='pink',
                                 command=self.open_mypeople)
        # self.person_btn.config(image=self.per_icon, compound=LEFT, width=5, height=10)
        self.person_btn.place(x=150, y=20)

        # Add People Button
        self.add_btn = Button(self.bottom, width=15, text="Add People", font="Times 12 bold", bg='pink', command=self.add_person)
        self.add_btn.place(x=150, y=60)

        # self.add_btn = Button(self.bottom, width=15, text="My People", font="Times 12 bold", bg='green')
        # self.person_btn.place(x=150, y=20)

    def open_mypeople(self):
        people = mypeople.MyPeople()

    def add_person(self):
        addpeople = addPeople.AddPeople()


def main():
    root = Tk()
    app = Application(root)
    root.title("Address Book")
    root.geometry("450x500+800+100")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
