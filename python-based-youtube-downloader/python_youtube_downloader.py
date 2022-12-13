import os
from pytube import YouTube, exceptions
from time import time
from tkinter import *
from customtkinter import *

# Tüm ayarları başlat
set_appearance_mode("System") # Görünüm modunu uygulama tarafından takip edilecek şekilde ayarlama: "Sistem", "Açık" veya "Koyu"
set_default_color_theme("blue") # takip edilecek uygulamanın temasını alma
for i in os.listdir(os.getcwd()):
    if i == "youtube_downloads": # Halihazırda "youtube_downloads" adlı bir klasör varsa yeni bir tane oluşturmayın
        break
else:    
    os.mkdir("youtube_downloads") # youtube_downloads" adında bir klasör yoksa yeni bir tane oluşturun

# Video işlevini indir
def download_video(entry_field):
    try:
        start_time = time()
        download_location = "youtube_downloads/"
        YouTube(entry_field).streams.first().download(download_location)
        end_time = time()

        # İndirme süresinin yeni bir pencerede gösterilmesi
        popup = CTk()
        popup.title("Download Status")
        popup.resizable(False, False)
        popup.geometry("200x100")
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure((0,1), weight=1)
        msg = StringVar()
        msg.set(f"Download successful!\nTotal time taken: {round(end_time-start_time,3)} seconds")
        label = CTkLabel(popup, text=msg.get())
        label.grid(row=0, column=0)
        button = CTkButton(popup, text="OK", command=popup.destroy)
        button.grid(row=1, column=0)
        popup.mainloop()
    except exceptions.RegexMatchError: # Geçersiz bir bağlantı veya boş bağlantı varsa, bir hata mesajı gösterin
        error = CTk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("300x100")
        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)
        error_label = CTkLabel(error, text="Please enter a valid YouTube link")
        error_label.grid(row=0, column=0)
        button = CTkButton(error, text="OK", command=error.destroy)
        button.grid(row=1, column=0)
        error.mainloop()

# Uygulamanın düzenini başlatıyor
master = CTk()
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("350x150")
master.resizable(False, False)
CTkLabel(master, text="Enter YouTube video URL:").grid(row=0, column=0)
entry = CTkEntry(master)
entry.grid(row=0, column=1)
CTkButton(master, text='Download', command=lambda *args: download_video(entry.get())).grid(row=1, column=0, columnspan=2)
master.mainloop()