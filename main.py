# YOUTUBE VIDEO DONWLOADER #
# https://stackoverflow.com/questions/10287683/python-convert-wav-to-mp3 #

from pytube import YouTube
import os
import subprocess
from colorama import Fore, Back, Style
from pydub import AudioSegment

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
#print(f"\n{Fore.GREEN}Rapporto like-dislike: {Style.RESET_ALL}", round(youTube.rating))               # rating



# Get the highest resolution #

resolution = input(f"\n{Style.RESET_ALL}Inserisci la risoluzione del video: {Fore.CYAN}")

ysVideo = youTube.streams.filter(res=resolution).first() #file_extension='mp4'
ysAudio = youTube.streams.filter(only_audio=True, file_extension='webm').first()



# download the video #

download = input(f"\n\n{Fore.YELLOW}Inserisci {Style.RESET_ALL}y {Fore.YELLOW}per scaricare, altrimenti qualsiasi altro carattere: {Style.RESET_ALL}")

title = youTube.title.replace('/', '-')

if str(download) == "y":
    try:
        os.mkdir("Downloads")
        print(f"\n{Fore.RED}\t--> Created Downloads folder. {Style.RESET_ALL}")
    except:
        print(f"\n{Fore.RED}\t--> No need to create Downloads folder. {Style.RESET_ALL}")

    try:
        os.mkdir("Downloads/" + str(title))
        print(f"\n{Fore.RED}\t--> Created video folder.{Style.RESET_ALL}")
    except:
        print(f"\n{Fore.RED}\t--> No need to create video folder. {Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}Download del video in corso...\nPuoi ignorare le seguenti scritte. Potrebbe doverti chiedere se tu voglia o no sovrascrivere il file già esistente.{Style.RESET_ALL}")

    video_name = str(title) + " [VIDEO ONLY].mp4"
    audio_name = str(title) + " [AUDIO ONLY].wav"

    out_video = ysVideo.download(filename="Downloads\\" + str(title) + "\\" + video_name)
    out_audio = ysAudio.download(filename="Downloads\\" + str(title) + "\\" + audio_name)

    os.chdir("Downloads/" + str(title))
    cmd = 'ffmpeg -i \"' + video_name + '\" -i \"' + audio_name + '\" -c:v copy -c:a aac \"' + str(title) + '\".mkv'
    print("\n" + cmd)
    subprocess.call(cmd, shell=False)

    '''sound = AudioSegment.from_mp3(audio_name)
    destName = str(title) + " [AUDIO ONLY].mp3"
    sound.export(destName, format="wav")'''

    link_file = open("Video Link.txt", "w")
    link_file.write(link)
    link_file.close()

    print(f"\n{Fore.YELLOW}Download completato! Troverai il tuo video nella cartella del programma \"Downloads/" + str(title) + f"\". {Style.RESET_ALL}")
else:
    print(f"\n{Fore.YELLOW}Fine programma.{Style.RESET_ALL}")