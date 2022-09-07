from asyncio import streams
import os
from pytube import YouTube
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.tix import Select
from webbrowser import get
from moviepy import *
from os import path
from pytube import *
import shutil
from moviepy.editor import *
from tkinter import messagebox
import pytube
import moviepy.editor
from tkinter.filedialog import *
from pytube import Playlist

screen = Tk()
title = screen.title('YouTube Downloader 2.0')
canvas = Canvas(screen, width=600, height=600)
canvas.pack()



#test
def download__file_mp3():
    if messagebox.askokcancel(title="Remember!!", message="You can't Download the same Audio in the Same Repertory, Check it Before The Downloading always. ") == True:
            messagebox.askokcancel(title="Are you sure ?" ,message="Are you sure you pasted the Audio link in the entry, if not press Cancel , Because if you don't do the Downloader freeze and The Audio  don't Downlaod ")
            path = filedialog.askdirectory()
            path_label.config(text=path)
            get__link = link__field.get()
            user__path = path_label.cget("text")
            
    else:
        pass    
    if messagebox.askokcancel(title="Download?", message="Press Ok to start The Downloading or Cancel to return") ==True:
            screen.title("Downloading , please wait a moment ..... ")
            mp3 = YouTube(get__link)
            mp3.streams.get_audio_only().download()            
            vid_clip = VideoFileClip(mp3)
            screen.title("YouTube Downloader 2.0")
            vid_clip.close
            shutil.move(mp3, user__path)
            screen.title("YouTube Downloader 2.0")
            messagebox.showinfo(title="Downlaod Complete!", message="Thanks for using our Downloader")
            messagebox.showinfo(title="Go!", message="Go to The Repertory where is The Audio Downloaded to make you sure is The video Downloaded ")        
            
    else:
            pass
    
  

def download__file():
    if messagebox.askokcancel(title="Remember!!", message="You can't Download the same Video in the Same Repertory, Check it Before The Downloading always. ") == True:
        messagebox.askokcancel(title="Are you sure ?" ,message="Are you sure you pasted the Video link in the entry, if not press Cancel , Because if you don't do the Downloader freeze and The file  don't Downlaod ")
        path = filedialog.askdirectory()
        path_label.config(text=path)
        get__link = link__field.get()
        user__path = path_label.cget("text")
    else:
        pass    
    if messagebox.askokcancel(title="Download?", message="Press Ok to start The Downloading or Cancel to return") ==True:
        screen.title("Downloading , please wait a moment ..... ")
        screen1 = Tk()
        title1 = screen1.title("Download, Please Wait a Moment .....")
        canvas = Canvas(screen, width=600, height=600)
        canvas.pack()
        mp4__video = YouTube(screen1,get__link).streams.get_highest_resolution().download()
        vid__clip =  VideoFileClip(screen1,mp4__video)
        vid__clip.close()
        shutil.move(mp4__video, user__path)
        messagebox.showinfo(title="Downlaod Complete!", message="Thanks for using our Downloader")
        messagebox.showinfo(title="Go!", message="Go to The Repertory where is The Video Downloaded to make you sure is The video Downloaded ")
        screen.title("YouTube Downloader 2.0")
    else:
        pass

def download_playlist():
        if messagebox.askokcancel(title="Remember!!", message="You can't Download the same Video in the Same Repertory, Check it Before The Downloading always. ") == True:
            messagebox.askokcancel(title="Are you sure ?" ,message="Are you sure you pasted the Video link in the entry, if not press Cancel , Because if you don't do the Downloader freeze and The file  don't Downlaod ")
            path = filedialog.askdirectory()
            path_label.config(text=path)
            get__link = link__field.get()
            user__path = path_label.cget("text")
        else:
            pass    
        if messagebox.askokcancel(title="Download?", message="Press Ok to start The Downloading or Cancel to return") ==True:
            screen.title("Downloading , please wait a moment ..... ")
            yt_playlist = Playlist(get__link)
            for video in yt_playlist.videos:
                video.streams.get_highest_resolution().download(user__path)
            vid__clip= VideoFileClip(yt_playlist)
            screen.title("YouTube Downloader 2.0")       
            vid__clip.close()
            shutil.move(yt_playlist, user__path)
            messagebox.showinfo(title="Downlaod Complete!", message="Thanks for using our Downloader")
            messagebox.showinfo(title="Go!", message="Go to The Repertory where is The Video Downloaded to make you sure is The video Downloaded ")
            
        else:
            pass

# image logo
logo__img = PhotoImage(file='Youtube-downloader/Photo Files/Youtube logo.png')
canvas.create_image(300, 100, image= logo__img)
# image logo 2
image_img_2 = PhotoImage(file="Youtube-downloader/Photo Files/youtube logo 2.png")
canvas.create_image(300,500, image=image_img_2)

# link field
link__field = Entry(screen,width=60)
canvas.create_window(300, 230, window=link__field)
#ctrl v label
Ctrl__v = Label(screen, text="Select The Link Entry and Press Ctrl+V to past The Link on ")
canvas.create_window(300,210, window=Ctrl__v)
# download btn
download__btn = Button(screen,bg="green" ,text="Download Video ", command=download__file)
canvas.create_window(300, 360, window=download__btn)
#link Label
link__label = Label(screen, text="Enter A Video link To download the Video", font=("Arial",15))
canvas.create_window(300, 170, window= link__label)
# download btn_mp3
download__btn_mp3 = Button(screen,bg="red" ,text="Download MP3 ", command=download__file_mp3)
canvas.create_window(300, 310, window=download__btn_mp3)
#playlist button
play_list = Button(screen, bg="yellow", text="Download Playlist", command=download_playlist)
canvas.create_window(300, 400, window=play_list)
#path label
path_label = Label(screen,text="And Press Download and choose a Repertory For the Download ", font=("Arial", 15))
canvas.create_window(300,280, window=path_label)
screen.mainloop()