import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Name'])
    e2.insert(0, select['Address'])
    e3.insert(0, select['Phone'])
    e4.insert(0, select['Email'])

def Add():
    name = e1.get()
    address = e2.get()
    phone = e3.get()
    email = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="lab_gacor")
    mycursor = mysqldb.cursor()
    try:
        sql = "INSERT INTO hotel_guest (Name, Address, Phone, Email) VALUES (%s, %s, %s, %s)"
        val = (name, address, phone, email)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record inserted successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
        show()  # Refresh the listbox
    except Exception as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()

def update():
    name = e1.get()
    address = e2.get()
    phone = e3.get()
    email = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="lab_gacor")
    mycursor = mysqldb.cursor()
    try:
        sql = "UPDATE hotel_guest SET Address = %s, Phone = %s, Email = %s WHERE Name = %s"
        val = (address, phone, email, name)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record updated successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
        show()  # Refresh the listbox
    except Exception as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()

def delete():
    name = e1.get()
    address = e2.get()
    phone = e3.get()
    email = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="lab_gacor")
    mycursor = mysqldb.cursor()
    try:
        sql = "DELETE FROM hotel_guest WHERE Name = %s OR Address =%s OR Phone = %s OR Email=%s"
        val = (name,address,phone, email)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("Information", "Record deleted successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
        show()  # Refresh the listbox
    except Exception as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="lab_gacor")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT Name, Address, Phone, Email FROM hotel_guest")
    records = mycursor.fetchall()
    listBox.delete(*listBox.get_children())
    for i, (name, address, phone, email) in enumerate(records, start=1):
        listBox.insert("", "end", values=(name, address, phone, email))
    mysqldb.close()

root = Tk()
root.geometry("800x500")
root.title("Hotel Guest Registration")

global e1, e2, e3, e4

tk.Label(root, text="Hotel Guest Registration", fg="blue", font=(None, 15)).place(x=250, y=5)
tk.Label(root, text="Name").place(x=10, y=50)
tk.Label(root, text="Address").place(x=10, y=80)
tk.Label(root, text="Phone").place(x=10, y=110)
tk.Label(root, text="Email").place(x=10, y=140)

e1 = Entry(root)
e1.place(x=140, y=50)
e2 = Entry(root)
e2.place(x=140, y=80)
e3 = Entry(root)
e3.place(x=140, y=110)
e4 = Entry(root)
e4.place(x=140, y=140)

Button(root, text="Add", command=Add, height=2, width=13).place(x=30, y=180)
Button(root, text="Update", command=update, height=2, width=13).place(x=140, y=180)
Button(root, text="Delete", command=delete, height=2, width=13).place(x=250, y=180)

cols = ('Name', 'Address', 'Phone', 'Email')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=230)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
