# YOUTUBE VIDEO DONWLOADER #

from pytube import YouTube
import os
import subprocess
from colorama import Fore, Back, Style
import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

'''
os.system("cls")
print(f"{Style.RESET_ALL}# {Fore.YELLOW}Benvenuto nel fantastico e miragicobolandiosissimo donwloader per YouTube! {Style.RESET_ALL}#")

link = input(f"\n{Style.RESET_ALL}Inserisci il link del video: {Fore.CYAN}")

try:
    youTube = YouTube(link)
except:
    print(f"\n{Fore.RED}Il link inserito non è valido.{Style.RESET_ALL}")
    exit()


# Retrieve video's informations #

print(f"\n\n{Style.RESET_ALL}# {Fore.YELLOW}IL TUO VIDEO {Style.RESET_ALL}#")
print(f"\n{Fore.GREEN}Titolo: {Style.RESET_ALL}", youTube.title)                                      # title
print(f"\n{Fore.GREEN}Autore: {Style.RESET_ALL}", youTube.author)                                     # author
print(f"\n{Fore.GREEN}Lunghezza: {Style.RESET_ALL}", round( int(youTube.length) / 60 , 2), " minuti") # length
print(f"\n{Fore.GREEN}Visualizzazioni: {Style.RESET_ALL}", youTube.views)                             # views
print(f"\n{Fore.GREEN}Rapporto like-dislike: {Style.RESET_ALL}", round(youTube.rating))               # rating



# Get the highest resolution #

ysVideo = youTube.streams.filter(adaptive=True, file_extension='mp4').first()
ysAudio = youTube.streams.filter(only_audio=True, file_extension='webm').first()



# download the video #

download = input(f"\n\n{Fore.YELLOW}Inserisci {Style.RESET_ALL}y {Fore.YELLOW}per scaricare, altrimenti qualsiasi altro carattere: {Style.RESET_ALL}")

if str(download) == "y":
    try:
        os.mkdir("Downloads")
        print(f"\n{Fore.RED}\t--> Created Downloads folder. {Style.RESET_ALL}")
    except:
        print(f"\n{Fore.RED}\t--> No need to create Downloads folder. {Style.RESET_ALL}")

    try:
        os.mkdir("Downloads/" + str(youTube.title))
        print(f"\n{Fore.RED}\t--> Created video folder.{Style.RESET_ALL}")
    except:
        print(f"\n{Fore.RED}\t--> No need to create video folder. {Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}Download del video in corso...{Style.RESET_ALL}")

    video_name = str(youTube.title) + " [VIDEO ONLY].mp4"
    audio_name = str(youTube.title) + " [AUDIO ONLY].wav"

    out_video = ysVideo.download(filename="Downloads\\" + str(youTube.title) + "\\" + video_name)
    out_audio = ysAudio.download(filename="Downloads\\" + str(youTube.title) + "\\" + audio_name)

    os.chdir("Downloads/" + str(youTube.title))
    cmd = 'ffmpeg -i \"' + video_name + '\" -i \"' + audio_name + '\" -c:v copy -c:a aac \"' + str(youTube.title) + '\".mkv'
    print("\n" + cmd)
    subprocess.call(cmd, shell=False)

    link_file = open("Video Link.txt", "w")
    link_file.write(link)
    link_file.close()

    print(f"\n{Fore.YELLOW}Download completato! Troverai il tuo video nella cartella del programma \"Downloads/" + str(youTube.title) + f"\". {Style.RESET_ALL}")
else:
    print(f"\n{Fore.YELLOW}Fine programma.{Style.RESET_ALL}")
'''