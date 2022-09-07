from tkinter import *
import sqlite3
from tkinter import messagebox
import addPeople

con = sqlite3.connect('pers_database')
cur = con.cursor()


def create_table():
    try:
        cur.execute("CREATE TABLE person(person_id integer primary key autoincrement, person_name text, email text, phone text, Address text)")
        con.commit()
    except:
        con.close()


create_table()


class MyPeople(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x500+800+100")
        self.title("My People")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white', relief=SUNKEN)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=410, bg="brown")
        self.bottom.pack(fill=X)

        # Headings, Images and Date
        self.top_image = PhotoImage(file=r"C:\Users\elcot\PycharmProjects\TkinterProjects\AddressBook\icons\person.png")
        self.top_image_lbl = Label(self.top, width=150, height=100, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=50, y=15)
        self.heading = Label(self.top, text="My People", fg='blue', bg='white', font="Times 15 bold")
        self.heading.place(x=230, y=50)

        # Scroll bar
        self.sb = Scrollbar(self.bottom, orient=VERTICAL)

        # List box
        self.listbox = Listbox(self.bottom, width=40, height=22)
        self.listbox.grid(row=0, column=0, padx=(40, 0))
        self.sb.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        persons = cur.execute("SELECT * FROM person").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.listbox.insert(count, f"{person[0]}-{person[1]}")
            count += 1

        # Buttons
        add_btn = Button(self.bottom, width=10, text="Add", font='Times 12 bold', bg='lightgreen',command=self.add_fun)
        add_btn.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        update_btn = Button(self.bottom, width=10, text="Update", font='Times 12 bold', bg='lightgreen', command=self.update_fun)
        update_btn.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        delete_btn = Button(self.bottom, width=10, text="Delete", font='Times 12 bold', bg='lightgreen', command=self.delete_fun)
        delete_btn.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        display_btn = Button(self.bottom, width=10, text="Display", font='Times 12 bold', bg='lightgreen', command=self.display_fun)
        display_btn.grid(row=0, column=2, sticky=N, padx=10, pady=130)

    def add_fun(self):
        add_people = addPeople.AddPeople()
        self.destroy()

    def update_fun(self):
        global person_id
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split("-")[0]
        update = Update()

    def display_fun(self):
        global person_id
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split("-")[0]
        dissplay = Display()

    def delete_fun(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split("-")[0]

        mbox = messagebox.askquestion("Delete", "Are you sure to delete!", icon="warning")
        if mbox == "yes":
            try:
                cur.execute("DELETE FROM person WHERE person_id=?", (person_id,))
                con.commit()
                messagebox.showinfo("Success", "Successfully deleted")
            except:
                messagebox.showinfo("Error", "person cant be deleted")


class Update(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x500+800+100")
        self.title("Update People")
        self.resizable(False, False)

        # get person from database
        global person_id
        person = cur.execute("SELECT * FROM person WHERE person_id=?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_email = person_info[0][2]
        self.person_phone = person_info[0][3]
        self.person_address = person_info[0][4]

        # Frames
        self.top = Frame(self, height=150, bg='white', relief=SUNKEN)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="pink")
        self.bottom.pack(fill=X)

        # Headings, Images and Date
        self.top_image = PhotoImage(
            file=r"C:\Users\elcot\PycharmProjects\TkinterProjects\AddressBook\icons\addpeople.png")
        self.top_image_lbl = Label(self.top, width=150, height=100, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=50, y=15)
        self.heading = Label(self.top, text="Update People", fg='blue', bg='white', font="Times 15 bold")
        self.heading.place(x=230, y=50)

        # Labels and Entries
        # Name
        self.name_lbl = Label(self.bottom, text="Name", font="Times 12 bold", bg='white', fg='brown')
        self.name_lbl.place(x=20, y=10)
        self.name_entry = Entry(self.bottom, width=25, bd=4)
        self.name_entry.insert(0, self.person_name)
        self.name_entry.place(x=100, y=10)

        # Email
        self.email_lbl = Label(self.bottom, text="Email", font="Times 12 bold", bg='white', fg='brown')
        self.email_lbl.place(x=20, y=50)
        self.email_entry = Entry(self.bottom, width=25, bd=4)
        self.email_entry.insert(0, self.person_email)
        self.email_entry.place(x=100, y=50)

        # Phone
        self.phone_lbl = Label(self.bottom, text="Phone", font="Times 12 bold", bg='white', fg='brown')
        self.phone_lbl.place(x=20, y=90)
        self.phone_entry = Entry(self.bottom, width=25, bd=4)
        self.phone_entry.insert(0, self.person_phone)
        self.phone_entry.place(x=100, y=90)

        # Address
        self.address_lbl = Label(self.bottom, text="Address", font="Times 12 bold", bg='white', fg='brown')
        self.address_lbl.place(x=20, y=130)
        self.address_entry = Text(self.bottom, width=25, height=8, bd=4, wrap=WORD)
        self.address_entry.insert('1.0', self.person_address)
        self.address_entry.place(x=100, y=130)

        # Button
        self.add_btn = Button(self.bottom, text="Update Person", font="Times 12 bold", bg="green", command=self.update_per)
        self.add_btn.place(x=160, y=280)

    def update_per(self):
        person_id = self.person_id
        person_name = self.name_entry.get()
        person_email = self.email_entry.get()
        person_phone = self.phone_entry.get()
        person_address = self.address_entry.get(1.0, "end-1c")

        try:
            query  = "UPDATE person set person_name=?, email=?, phone=?, Address=? WHERE person_id=?"
            cur.execute(query, (person_name, person_email, person_phone, person_address,person_id))
            con.commit()
            messagebox.showinfo("Successful", "Successfully Updated!")
            self.destroy()
        except:
            messagebox.showerror("Error", "Can't update to database", icon="warning")


class Display(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x500+800+100")
        self.title("Display Person")
        self.resizable(False, False)

        # get person from database
        global person_id
        person = cur.execute("SELECT * FROM person WHERE person_id=?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_email = person_info[0][2]
        self.person_phone = person_info[0][3]
        self.person_address = person_info[0][4]

        # Frames
        self.top = Frame(self, height=150, bg='white', relief=SUNKEN)
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=400, bg="pink")
        self.bottom.pack(fill=X)

        # Headings, Images and Date
        self.top_image = PhotoImage(
            file=r"C:\Users\elcot\PycharmProjects\TkinterProjects\AddressBook\icons\person.png")
        self.top_image_lbl = Label(self.top, width=150, height=100, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=50, y=15)
        self.heading = Label(self.top, text="Display Person", fg='blue', bg='white', font="Times 15 bold")
        self.heading.place(x=230, y=50)

        # Labels and Entries
        # Name
        self.name_lbl = Label(self.bottom, text="Name", font="Times 12 bold", bg='white', fg='brown')
        self.name_lbl.place(x=20, y=10)
        self.name_entry = Entry(self.bottom, width=25, bd=4)
        self.name_entry.insert(0, self.person_name)
        self.name_entry.config(state='disabled')
        self.name_entry.place(x=100, y=10)

        # Email
        self.email_lbl = Label(self.bottom, text="Email", font="Times 12 bold", bg='white', fg='brown')
        self.email_lbl.place(x=20, y=50)
        self.email_entry = Entry(self.bottom, width=25, bd=4)
        self.email_entry.insert(0, self.person_email)
        self.email_entry.config(state='disabled')
        self.email_entry.place(x=100, y=50)

        # Phone
        self.phone_lbl = Label(self.bottom, text="Phone", font="Times 12 bold", bg='white', fg='brown')
        self.phone_lbl.place(x=20, y=90)
        self.phone_entry = Entry(self.bottom, width=25, bd=4)
        self.phone_entry.insert(0, self.person_phone)
        self.phone_entry.config(state='disabled')
        self.phone_entry.place(x=100, y=90)

        # Address
        self.address_lbl = Label(self.bottom, text="Address", font="Times 12 bold", bg='white', fg='brown')
        self.address_lbl.place(x=20, y=130)
        self.address_entry = Text(self.bottom, width=25, height=8, bd=4, wrap=WORD)
        self.address_entry.insert('1.0', self.person_address)
        self.address_entry.config(state='disabled')
        self.address_entry.place(x=100, y=130)