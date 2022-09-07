from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('pers_database')
cur = con.cursor()


class AddPeople(Toplevel):
    per_id = 0

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x500+800+100")
        self.title("Add People")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white', relief=SUNKEN)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="pink")
        self.bottom.pack(fill=X)

        # Headings, Images and Date
        self.top_image = PhotoImage(file=r"C:\Users\elcot\PycharmProjects\TkinterProjects\AddressBook\icons\addpeople.png")
        self.top_image_lbl = Label(self.top, width=150, height=100, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=50, y=15)
        self.heading = Label(self.top, text="Add People", fg='blue', bg='white', font="Times 15 bold")
        self.heading.place(x=230, y=50)

        # Labels and Entries
        # Name
        self.name_lbl = Label(self.bottom, text="Name", font="Times 12 bold", bg='white', fg='brown')
        self.name_lbl.place(x=20, y=10)
        self.name_entry = Entry(self.bottom, width=25, bd=4)
        self.name_entry.insert(0, "Please Enter your Name")
        self.name_entry.place(x=100, y=10)

        # Email
        self.email_lbl = Label(self.bottom, text="Email", font="Times 12 bold", bg='white', fg='brown')
        self.email_lbl.place(x=20, y=50)
        self.email_entry = Entry(self.bottom, width=25, bd=4)
        self.email_entry.insert(0, "Please Enter your Email")
        self.email_entry.place(x=100, y=50)

        # Phone
        self.phone_lbl = Label(self.bottom, text="Phone", font="Times 12 bold", bg='white', fg='brown')
        self.phone_lbl.place(x=20, y=90)
        self.phone_entry = Entry(self.bottom, width=25, bd=4)
        self.phone_entry.insert(0, "Please Enter your Number..")
        self.phone_entry.place(x=100, y=90)

        # Address
        self.address_lbl = Label(self.bottom, text="Address", font="Times 12 bold", bg='white', fg='brown')
        self.address_lbl.place(x=20, y=130)
        self.address_entry = Text(self.bottom, width=25, height=8, bd=4, wrap=WORD)
        self.address_entry.place(x=100, y=130)

        # Button
        self.add_btn = Button(self.bottom, text="Add Person", font="Times 12 bold", bg="green", command=self.addperson)
        self.add_btn.place(x=160, y=280)

    def addperson(self):
        AddPeople.per_id += 1
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get(1.0, "end-1c")
        if (name and email and phone and address) != "":
            try:
                query = "INSERT INTO 'person'(person_name,email,phone,Address) VALUES(?,?,?,?)"
                cur.execute(query, (name, email, phone, address))
                con.commit()
                con.close()
                messagebox.showinfo("Successful", "Successfully added")

            except:
                messagebox.showerror("Error", "Cant add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon="warning")

