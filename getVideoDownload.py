"""
Created on Sun May 16 11:29:03 2021

@author: KashyapParmar
"""
from tkinter import *
import tkinter as tk
import pytube
from urllib.request import HTTPError
from pytube import YouTube  
from downloadYTVideos import VideoTitleGet,downloadMainFunction

    
def LoginSuccess(username):    
    from tkinter import ttk
    window = tk.Tk()
    window.title("YouTube Video Downloader")
    window.geometry('900x900')
    
    window.configure(background = "grey")
    URL_Label = Label(window ,text = "Paste URL Link of Video Here -->:").grid(row = 3,column = 0)
    name = Label(window ,text = 'Hi '+ username ,font=('Arial',12, 'bold'),width=20,bg='white', fg='green').grid(row = 0,column = 0)
    name2 = Label(window ,text = 'Paste URL of the Youtube Video below ',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 1,column = 0)
    
    
    URL_Entry = Entry(window,width=60)
    URL_Entry.grid(row = 3,column = 1)
    
    
    
    def clicked():
        videoInfoList=[]
        videoInfoList,streamsList = VideoTitleGet(URL_Entry.get())
        if len(videoInfoList)==0 or len(streamsList)==0: 
            videoNotFoundLabel = Label(window ,text = 'Video Not Found ! Incorrect URL Provided',font=('Arial',12, 'bold'),bg='white', fg='red').grid(row = 10,column = 1)
            internetLabel  = Label(window ,text = 'OR There is not Stable Internet Connection, PRESS SEARCH BUTTON AGAIN',font=('Arial',10, 'bold'),bg='white', fg='red').grid(row = 11,column = 1)
            
        else:
            if videoInfoList[7]==False:ageRest="No"
            else:ageRest="Yes"
            
            videoNotFoundLabel = Label(window ,text = 'Video Not Found ! Incorrect URL Provided',font=('Arial',12, 'bold'),bg='#2196F3', fg='#2196F3').grid(row = 10,column = 1)
            internetLabel  = Label(window ,text = 'OR There is not Stable Internet Connection, PRESS SEARCH BUTTON AGAIN',font=('Arial',10, 'bold'),bg='#2196F3', fg='#2196F3').grid(row = 11,column = 1)

            videoFoundLabel = Label(window ,text = 'Video Found on Youtube!!!',font=('Arial',12, 'bold'),bg='white', fg='red').grid(row = 1,column = 1)
            
            video_title = Label(window ,text = 'Video Title --> ',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 10,column = 0)
            video_description =  Label(window ,text = 'Video Description -->',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 11,column = 0)
            video_length =  Label(window ,text = 'Video Length -->',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 12,column = 0)
            video_views =  Label(window ,text = 'Video Views -->',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 13,column = 0)
            video_age_rest =  Label(window ,text = 'Age Restriction (Yes/No) -->',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 14,column = 0)
            video_resolutions =  Label(window ,text = 'Downloadable Resolutions -->',font=('Arial',8, 'bold'),bg='white', fg='green').grid(row = 15,column = 0)
            
            
            lbl1 = Label(window ,text = str(videoInfoList[0]) ,font=('Arial',8, 'bold'), bg='black',fg='white').grid(row = 10,column = 1)
            lbl2 = Label(window ,text = str(videoInfoList[2]),font=('Arial',8, 'bold'), bg='black',fg='white').grid(row = 11,column = 1)
            lbl3 = Label(window ,text = str(videoInfoList[3])+" seconds" ,font=('Arial',8, 'bold'), bg='black',fg='white').grid(row = 12,column = 1)
            lbl4 = Label(window ,text = str(videoInfoList[5])+" views" ,font=('Arial',8, 'bold'), bg='black',fg='white').grid(row = 13,column = 1)
            lbl5 = Label(window ,text = ageRest ,font=('Arial',8, 'bold'), bg='black',fg='white').grid(row = 14,column = 1)
            window.configure(background='#2196F3')
            n = tk.StringVar()
            resChoosen = ttk.Combobox(window, width = 80, textvariable = n)
            streamsTuple = tuple(streamsList)
            resChoosen['values'] = streamsTuple
            resChoosen.grid(row = 15,column = 1) 
            resChoosen.current(1)       
            
            def clickedDownload():
                
                resString = str(resChoosen.get())
                i=15
                passingStr=''
                while resString[i]!='"':
                    passingStr = passingStr+ resString[i]
                    i=i+1
                resInt = int(passingStr)
                
                returnStr = downloadMainFunction(videoInfoList,URL_Entry.get(),resInt)
                

                if returnStr=="An Error Occured":
                    videoFoundLabel = Label(window ,text = "Not Stable Internet Connection, PRESS DOWNLOAD BUTTON AGAIN",font=('Arial',8, 'bold'),bg='white', fg='red').grid(row = 16,column = 1)
                elif returnStr[0:33:1]=="File already exists at Location :":
                    
                    videoFoundLabel = Label(window ,text = "File already exists at Location --> ",font=('Arial',12, 'bold'),bg='white', fg='red').grid(row = 16,column = 0)
                    Location_Entry = Entry(window,width=60)
                    Location_Entry.grid(row = 16,column = 1)
                    Location_Entry.insert(0,returnStr[33::1])
                else:
                    videoFoundLabel = Label(window ,text = "File Saved Successfully at Location --> ",font=('Arial',12, 'bold'),bg='white', fg='red').grid(row = 16,column = 0)
                    Location_Entry = Entry(window,width=60)
                    Location_Entry.grid(row = 16,column = 1)
                    Location_Entry.insert(0,returnStr[23::1])
                
                
            btn2 = ttk.Button(window ,text="Download",command=clickedDownload).grid(row=9,column=1)
            hereDownloadLabel = Label(window ,text = "<--Press here to Download",font=('Arial',8, 'bold'),bg='white', fg='red').grid(row = 9,column = 2)

            #btn3=  ttk.Button(window,text = 'Download', command = clickedDownload,  font = ('Times', 12, 'bold'),bg='#00FF00', fg='black',relief='groove', justify = 'center', pady='5'  ).grid(row=15,column=1) 

            
    btn = ttk.Button(window ,text="Search",command=clicked).grid(row=9,column=1)
    window.mainloop()
