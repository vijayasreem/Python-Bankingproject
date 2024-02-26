from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox

class PROFILE:

    def show_m(self):
        self.profframe.grid_forget()
        self.menu.grid(padx=self.ws * 0.3, pady=self.hs * 0.2)

    def show_profile(self):
        self.menu.grid_forget()
        self.profframe = tk.Frame(self.master, bg='gray')
        try:
            db = sql.connect('localhost', 'bank', 'bank', 'bank')
            c = db.cursor()
            c.execute('select * from user where name="{}"'.format(self.user))
            data = c.fetchone()
            self.udname = StringVar()
            self.udpass = StringVar()
            self.udacc = StringVar()
            self.udbal = StringVar()
            self.udname.set(data[1])
            self.udpass.set(data[2])
            self.udacc.set(data[0])
            self.udbal.set(data[3])
        except Exception as e:
            messagebox.showerror('DataBASE Connectivity', '!!Error!!Database Connection!!{}'.format(e))
            exit(0)
        self.p_l1 = Label(self.profframe, text='Account No:{}'.format(self.udacc.get()), bg='gray', font=('Times', '18', 'bold'), fg='#ffffff')
        self.p_l1.grid(row=0, column=0, columnspan=2, padx=64)
        self.p_l2 = Label(self.profframe, text='User Name:{}'.format(self.udname.get()), bg='gray', font=('Times', '18', 'bold'), fg='#ffffff')
        self.p_l2.grid(row=1, column=0, columnspan=2, padx=64)
        self.p_l3 = Label(self.profframe, text='Balance:{}'.format(self.udbal.get()), bg='gray', font=('Times', '18', 'bold'), fg='#ffffff')
        self.p_l3.grid(row=2, column=0, columnspan=2, padx=64)
        self.p_b1 = tk.Button(self.profframe, text='Change Name', bg='#777777', font=('Times', '20', 'bold'), width=13, command=self.updatename, fg='#003b8b')
        self.p_b1.grid(row=3, column=0, padx=64, pady=19)
        self.p_b2 = tk.Button(self.profframe, text='Change Password', bg='#777777', font=('Times', '20', 'bold'), width=13, command=self.change_password, fg='#003b8b')
        self.p_b2.grid(row=4, column=0, padx=64, pady=10)
        self.p_b3 = tk.Button(self.profframe, text='Edit Profile', bg='#777777', font=('Times', '20', 'bold'), width=13, command=self.edit_profile, fg='#003b8b')
        self.p_b3.grid(row=5, column=0, padx=64, pady=10)
        self.p_b4 = tk.Button(self.profframe, text='<<Back', width=10, bg='#777777', font=('Times', '18', 'bold'), command=self.show_m, fg='#000000')
        self.p_b4.grid(row=6, column=1, padx=64, pady=18)
        self.profframe.grid(padx=self.ws * 0.3, pady=self.hs * 0.2)

    def edit_profile(self):
        self.profframe.grid_forget()
        self.editframe = tk.Frame(self.master, bg='gray')
        self.edit_name_lbl = Label(self.editframe, text='New UserName:', bg='gray', font=('Times', '20', 'bold'), fg='#ffffff')
        self.edit_name_lbl.grid(row=0, column=0, padx=30)
        self.edit_name = Entry(self.editframe, bg='#123456', width=20, font=('Times', '20', 'bold'), fg='#FFFFFF')
        self.edit_name.grid(row=0, column=1, padx=40)
        self.edit_pass_lbl = Label(self.editframe, text='New Password:', bg='gray', font=('Times', '20', 'bold'), fg='#ffffff')
        self.edit_pass_lbl.grid(row=1, column=0, padx=30)
        self.edit_pass = Entry(self.editframe, bg='#123456', width=20, font=('Times', '20', 'bold'), fg='#FFFFFF')
        self.edit_pass.grid(row=1, column=1, padx=40)
        self.edit_b1 = tk.Button(self.editframe, text='Update', bg='gray', width=14, font=('Times', '20', 'bold'), command=self.update_profile, fg='#000000')
        self.edit_b1.grid(row=2, column=1, padx=67, pady=10, columnspan=2)
        self.edit_b2 = tk.Button(self.editframe, text='<<Back', bg='gray', font=('Times', '20', 'bold'), command=self.show_m1, fg='#000000')
        self.edit_b2.grid(row=3, column=0, pady=15, padx=10)
        self.editframe.grid(padx=self.ws * 0.3, pady=self.hs * 0.2)

    def update_profile(self):
        try:
            if self.edit_name.get() and self.edit_pass.get():
                name = self.edit_name.get()
                password = self.edit_pass.get()
                db = sql.connect('localhost', 'bank', 'bank', 'bank')
                c = db.cursor()
                c.execute('update user set name="{}", password="{}" where name="{}"'.format(name, password, self.user))
                db.commit()
                c.close()
                db.close()
                messagebox.showinfo('!!Sucess!!', 'Updated User Profile Sucessfully')
                self.editframe.grid_forget()
                self.user = name
                self.udname.set(name)
                self.udpass.set(password)
                self.menu.grid(padx=self.ws * 0.3, pady=self.hs * 0.2)
            else:
                messagebox.showerror('InputError', 'Error!!Please Enter new username and password')
        except Exception as e:
            messagebox.showerror('Error!!', e)

    # Rest of the code remains the same
