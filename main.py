import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import yt_dlp as ytdlp

# Initialize Tkinter window
screen = tk.Tk()
screen.title('YouTube Downloader 2.0, nibras09')
canvas = tk.Canvas(screen, width=600, height=360)
canvas.pack()

def download_file_mp3():
    if messagebox.askokcancel(title="Remember!!", message="You can't download the same mp3 file in the same directory, check before the download begins."):

        if messagebox.askokcancel(title="Are you sure?", message="Are you sure you pasted the mp3 file link in the entry? If not, press Cancel."):

            path = filedialog.askdirectory()
            path_label.config(text=path)
            get_link = link__field.get()

            if not get_link:
                messagebox.showerror(title="Error", message="No link provided.")
                return

            screen.title("Downloading, please wait a moment...")

            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{path}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            try:
                with ytdlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([get_link])
                messagebox.showinfo(title="Download Complete!", message="Thanks for using our program.")
                messagebox.showinfo(title="Go!", message="Go to the directory where the audio was downloaded to verify the file.")
            except Exception as e:
                messagebox.showerror(title="Download Error", message=f"An error occurred: {e}")

            screen.title("YouTube Downloader 2.0")

def download_file():
    if messagebox.askokcancel(title="Remember!!", message="You can't download the same video in the same directory. Check it before downloading."):

        if messagebox.askokcancel(title="Are you sure?", message="Are you sure you pasted the video link in the entry? If not, press Cancel."):

            path = filedialog.askdirectory()
            path_label.config(text=path)
            get_link = link__field.get()

            if not get_link:
                messagebox.showerror(title="Error", message="No link provided.")
                return

            screen.title("Downloading, please wait a moment...")

            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{path}/%(title)s.%(ext)s',
            }

            try:
                with ytdlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([get_link])
                messagebox.showinfo(title="Download Complete!", message="Thanks for using our Downloader.")
                messagebox.showinfo(title="Go!", message="Go to the directory where the video was downloaded to verify the file.")
            except Exception as e:
                messagebox.showerror(title="Download Error", message=f"An error occurred: {e}")

            screen.title("YouTube Downloader 2.0")

def download_playlist():
    if messagebox.askokcancel(title="Remember!!", message="You can't download the same video in the same directory. Check it before downloading."):

        if messagebox.askokcancel(title="Are you sure?", message="Are you sure you pasted the playlist link in the entry? If not, press Cancel."):

            path = filedialog.askdirectory()
            path_label.config(text=path)
            get_link = link__field.get()

            if not get_link:
                messagebox.showerror(title="Error", message="No link provided.")
                return

            screen.title("Downloading, please wait a moment...")

            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{path}/%(playlist_title)s/%(title)s.%(ext)s',
                'noplaylist': False,  # Ensure playlist mode is enabled
            }

            try:
                with ytdlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([get_link])
                messagebox.showinfo(title="Download Complete!", message="Thanks for using our Downloader.")
                messagebox.showinfo(title="Go!", message="Go to the directory where the videos were downloaded to verify the files.")
            except Exception as e:
                messagebox.showerror(title="Download Error", message=f"An error occurred: {e}")

# Load the image
image_path2 = os.path.join(os.path.dirname(__file__), 'youtube logo 2.png')
try:
    pil_image2 = Image.open(image_path2)
    image2 = ImageTk.PhotoImage(pil_image2)
    label2 = tk.Label(screen, image=image2)
    label2.place(x=300, y=300)
    label2.pack()
except Exception as e:
    print(f"Error loading image2: {e}")

# Link field
link__field = tk.Entry(screen, width=60)
canvas.create_window(300, 200, window=link__field)

# Ctrl+V label
Ctrl__v = tk.Label(screen, text="Select The Link Entry and Press Ctrl+V to paste the link.")
canvas.create_window(300, 140, window=Ctrl__v)

# Download Video button
download__btn = tk.Button(screen, bg="green", text="Download Video", command=download_file)
canvas.create_window(300, 290, window=download__btn)

# Link Label
link__label = tk.Label(screen, text="Enter a Video link to download the video", font=("Arial", 15))
canvas.create_window(300, 100, window=link__label)

# Download MP3 button
download__btn_mp3 = tk.Button(screen, bg="red", text="Download MP3", command=download_file_mp3)
canvas.create_window(300, 240, window=download__btn_mp3)

# Playlist button
play_list = tk.Button(screen, bg="yellow", text="Download Playlist", command=download_playlist)
canvas.create_window(300, 330, window=play_list)

# Path Label
path_label = tk.Label(screen, text="Press Download and choose a directory for the download", font=("Arial", 15))
canvas.create_window(300, 180, window=path_label)

screen.mainloop()