# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:29:03 2021

@author: KashyapParmar
"""
#
#import os
#import pytube
#from urllib.request import HTTPError
def VideoTitleGet(URLString):  
    import os
    import pytube
    from urllib.request import HTTPError

    videoInfoList=[]
    streamsList=[]
    try:
        from pytube import YouTube  
        video = YouTube(URLString)  
        videoInfoList.append(video.title)  
        videoInfoList.append(video.video_id)  
        videoInfoList.append(video.description)  
        videoInfoList.append(video.length)  
        videoInfoList.append(video.thumbnail_url)  
        videoInfoList.append(video.views)  
        videoInfoList.append(video.rating)  
        videoInfoList.append(video.age_restricted)
        streamsList=video.streams.all()
        return videoInfoList,streamsList
    except Exception:
        videoInfoList=[]
        return videoInfoList,streamsList
        

def downloadMainFunction(videoInfoList,URLVideo,resInt):
    import os
    import pytube
    from urllib.request import HTTPError

    if os.path.isfile(r"C:/YTVideoDir/"+videoInfoList[0]+".mp4"):
        return "File already exists at Location :"+"C:/YTVideoDir/"+videoInfoList[0]+".mp4"
    else:
        try:       
            str1="C:\\YTVideoDir\\"
            video_url = URLVideo   
            youtube = pytube.YouTube(video_url)  
            print(1)
            #out_file = youtube.streams.first().download(str1)
            out_file = youtube.streams.get_by_itag(resInt).download(str1)

            print(2)
            print(3)
            print(4)
            print('Video Downloaded successfully !')
            return 'File Saved in Location:'+str1+videoInfoList[0]+".mp4"
        except HTTPError:
            print("HTTPError Occurerd...") 
            return "Press Donload Button Again"
