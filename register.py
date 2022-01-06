"""
Created on Sun May 16 11:29:03 2021

@author: KashyapParmar
"""
# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

# Creating register function
def Register():
    
    # Creating a new window
    Reg = tk.Tk()
    Reg.title('Register in System')
    Reg.geometry('700x700')

    # Background Colors
    Reg.configure(background='#2196F3')

    # Locking the window size
    Reg.resizable(width=False, height=False)

    # Creating title icon
    Reg.iconbitmap('img/reglogo.ico')
    
    # Top Frame
    top_frame = Label(Reg, text='Registration',font = ('Cosmic', 25, 'bold'), bg='#2196F3',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Connecting to database with registration form
    def database(arg=None):
      
        # Getting entries
        name = name_entry.get()
        email = email_entry.get()

        # Mobile Number converting to Integer
        mobile = mobile_entry.get()
        try:
            mobile = int(mobile)
        except:
            ms.showerror('Oops', 'Please Enter a Valid Phone Number !!!')

        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(name)
        validation.append(email)
        validation.append(mobile)
        validation.append(username)
        validation.append(password)
        validation.append(confirm)

        # Boolean for condition
        condition = True
        
        # Looping and checking conditions
        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:
            
            # Checking for password match
            if password != confirm:
                ms.showerror('Oops', 'Password Does Not Match!!!')    
                
            else:
                # Making connection
                conn = sqlite3.connect('Database.db')

                #Creating cursor
                with conn:
                    cursor = conn.cursor()

                # Making table if not exist
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (FullName TEXT NOT NULL, Email TEXT NOT NULL, Mobile TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)')

                # Inserting Data into Table
                cursor.execute('INSERT INTO Users (FullName, Email, Mobile, Username, Password) VALUES (?,?,?,?,?)', (name, email, mobile, username, password))
                conn.commit()

                # Showing success message
                ms.showinfo('Successful', 'Account Created Successfully!! Now You Can Login To System!!')

                # Closing the window
                Reg.destroy()
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields')
    
    # creating a label for username and password using Label
    name = tk.Label(frame, text = 'Full Name', font=('Arial',12, 'bold'), bg='white', fg='green')
    email = tk.Label(frame, text = 'Email', font=('Arial',12, 'bold'), bg='white', fg='green')
    mobile = tk.Label(frame, text = 'Mobile No.', font=('Arial',12, 'bold'), bg='white', fg='green')
    username = tk.Label(frame, text = 'Username', font=('Arial',12, 'bold'), bg='white', fg='green')                    
    password = tk.Label(frame, text = 'Password', font = ('Arial',12,'bold'), bg='white', fg='green')
    confirm = tk.Label(frame, text = 'Confirm Password', font=('Arial',12, 'bold'), bg='white', fg='green')

    # creating a entry for elements and returning values to the databse function
    name_entry = tk.Entry(frame ,font=('Arial',12,'normal'), bg='#00FFFF')
    name_entry.bind("<Return>", database)
    email_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#00FFFF')
    email_entry.bind("<Return>",database)
    mobile_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#00FFFF')
    mobile_entry.bind("<Return>",database)
    username_entry = tk.Entry(frame,font=('Arial',12,'normal'), bg='#00FFFF')
    username_entry.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#00FFFF')
    password_entry.bind("<Return>",database)
    confirm_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#00FFFF')
    confirm_entry.bind("<Return>",database)
       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Register', command = database, width="10",bd = '3',  font = ('Times', 12, 'bold'),bg='#00FF00', fg='black',relief='groove', justify = 'center', pady='5'  ) 
       
    # Placing the label and entry
    name.pack()
    name_entry.focus_set()
    name_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    email.pack()
    email_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    mobile.pack()
    mobile_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    username.pack() 
    username_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    confirm.pack()
    confirm_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Reg, text = "Quit", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
