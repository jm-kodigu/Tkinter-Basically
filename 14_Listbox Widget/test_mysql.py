from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="jmq123jj",
	database="tkinter"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM estudent")

result = mycursor.fetchall()

master = Tk()
master.iconbitmap(r"C:/Users/Juliao JM/Downloads/py-white.ico")
master.title("Listbox Widget")
master.geometry("400x200")

l = Listbox(master)
l.pack()

l.delete(0, END)

for x in result:
	l.insert(END, x[1])


master.mainloop()