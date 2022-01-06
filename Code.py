"""
Created on Sun May 16 11:29:03 2021

@author: KashyapParmar
"""
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from login import Log
from register import Register
from PIL import ImageTk, Image
import os
  
directory = "YTVideoDir"
parent_dir = "/home/hitmanbolt/Desktop/GOLANG/IIT BHU INTERNSHIP/YoutubeVideoDowloaderUsingPython"
path = os.path.join(parent_dir, directory)
  
try:
    os.mkdir(path)
except Exception:
    pass
  
''' Window Setting Start '''
system = tk.Tk()

system.geometry('500x500')

system.configure(background='#2196F3')

system.resizable(width=False, height=False)
system.title('YouTube Video Downloader App')

system.iconbitmap(r'./home/hitmanbolt/Desktop/GOLANG/IIT BHU INTERNSHIP/YoutubeVideoDowloaderUsingPython/img/logo.ico')
''' Window Setting End '''

top_frame = Label(system, text='Welcome to YouTube Video Downloader App',font = ('Cosmic', 13, 'bold'), bg='#2196F3',relief='groove',padx=500, pady=30)
top_frame.pack(side='top')


''' Background Image Start'''
# Sizing Image
canvas = Canvas(system, width=500, height=350)

image = ImageTk.PhotoImage(Image.open('img/back.jpg'))

canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()
''' Background Image End'''

frame = LabelFrame(system,text='Please Enter Credentials', padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


login = tk.Button(frame, text = "Login", width="10", bd = '3', command = Log, font = ('Times', 12, 'bold'), bg='#00FF00',relief='groove', justify = 'center', pady='5')
login.pack()

label = Label(frame, bg='white').pack()

register = tk.Button(frame, text = "Register", width="10", bd = '3',  command = Register, font = ('Times', 12, 'bold'), bg='#00FF00',fg='black', relief='groove', justify = 'center', pady='5')
register.pack()


def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        system.destroy()
    else:
        pass
    
Quit = tk.Button(system, text = "Quit", width="10", command = Quit, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.775)

system.mainloop()
    
