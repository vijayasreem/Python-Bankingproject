from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
import csv

class CREDIT():
    
    def credit_Balance(self):

        self.menu.grid_forget()

        self.credframe = tk.Frame(self.master,bg="#777777")

        self.up_amnt_lbl1 = Label(self.credframe,text='Welcome {} to Credit Services'.format(self.user),bg="#777777",font=('Times','20','bold'),fg="#ffffff")
        self.up_amnt_lbl1.grid(row=0,column=0,columnspan=2,pady=10)

        self.up_amnt_lbl2 = Label(self.credframe,text='Enter amount to credit',bg="#777777",font=('Times','26','bold'),fg="#ffffff")
        self.up_amnt_lbl2.grid(row=1,column=0,columnspan=2,pady=10)

        self.up_amnt_lbl = Label(self.credframe,text='Amount',bg="#777777",font=('Times','25','bold'),fg="#ffffff")
        self.up_amnt_lbl.grid(row=2,column=0,pady=10)

        self.up_amnt = Entry(self.credframe,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_amnt.grid(row=2,column=1,pady=10,padx=30)

        self.up_amnt_btn = tk.Button(self.credframe,text='update balance',bg="#777777",font=('Times','20','bold'),width=15,command=self.credit,fg="#000000")
        self.up_amnt_btn.grid(row=3,column=1,pady=13,padx=72)

        self.up_amnt_btn1 = tk.Button(self.credframe,text='<<Back',bg="#777777",font=('Times','18','bold'),command=self.show_m5,fg="#000000",width=10)
        self.up_amnt_btn1.grid(row=4,column=0,pady=16,padx=40)

        self.view_history_btn = tk.Button(self.credframe,text='View Balance History',bg="#777777",font=('Times','18','bold'),command=self.view_balance_history,fg="#000000",width=20)
        self.view_history_btn.grid(row=4,column=1,pady=16,padx=40)

        self.credframe.grid(padx=self.ws*.3,pady=self.hs*.2)

    def credit(self):
        if self.up_amnt.get():
            try :
                amount = float(self.up_amnt.get())
                amnt=self.up_amnt.get()
                db = sql.connect('localhost','bank','bank','bank')
                c = db.cursor()
                c.execute('select balance from user where name="{}"'.format(self.user))
                bal = c.fetchone()[0]
                cmd="update user SET balance=balance+{} where name='{}'".format(amnt,self.user)
                c.execute(cmd)
                db.commit()
                c.close()
                db.close()
                s='Sucessfully {} rs credited to the account associated with {}.\nYour Updated Balance is now {}.'.format(amount,self.user,amount+bal)
                messagebox.showinfo("CREDIT",s)
                self.credframe.grid_forget()
                self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

            except ValueError as e :
                messagebox.showerror("!!Input Error!!","Please Enter a Valid Amount")
        else :
            messagebox.showerror("!!Input Error!!","Please Enter Some Amount to Credit")

    def show_m5(self):
        self.credframe.grid_forget()
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)
        
    def view_balance_history(self):
        db = sql.connect('localhost','bank','bank','bank')
        c = db.cursor()
        c.execute('select * from balance_history where user="{}"'.format(self.user))
        history = c.fetchall()
        c.close()
        db.close()
        
        self.history_frame = tk.Frame(self.master,bg="#777777")
        
        self.history_lbl = Label(self.history_frame,text='Balance History',bg="#777777",font=('Times','20','bold'),fg="#ffffff")
        self.history_lbl.grid(row=0,column=0,columnspan=3,pady=10)
        
        self.history_table = tk.Text(self.history_frame, height=10, width=50)
        self.history_table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.download_btn = tk.Button(self.history_frame,text='Download as CSV',bg="#777777",font=('Times','18','bold'),command=self.download_balance_history,fg="#000000",width=15)
        self.download_btn.grid(row=2,column=1,pady=16,padx=40)
        
        self.history_table.insert(tk.END, "Date\tAmount\tRunning Balance\n")
        for entry in history:
            self.history_table.insert(tk.END, "{}\t{}\t{}\n".format(entry[0], entry[1], entry[2]))
        
        self.history_frame.grid(padx=self.ws*.3,pady=self.hs*.2)
        
    def download_balance_history(self):
        db = sql.connect('localhost','bank','bank','bank')
        c = db.cursor()
        c.execute('select * from balance_history where user="{}"'.format(self.user))
        history = c.fetchall()
        c.close()
        db.close()
        
        with open('balance_history.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Running Balance"])
            writer.writerows(history)
        
        messagebox.showinfo("Download", "Balance history downloaded as CSV file.")
        

# Create an instance of the CREDIT class and run the application
root = tk.Tk()
app = CREDIT(root)
root.mainloop()