from pytube import YouTube
from pytube import Playlist
import validators


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Download():

    #GET USER CHOICE
    form = input("SELECT A FORMAT :\n1. FOR VIDEO\n2. FOR ONLY AUDIO\n3. FOR PLAYLIST\n"
                 "YOUR CHOICE : ")
    #GET USER VIDEO URL
    vid_url = input("URL => ")
    #VALIDATE URL
    check_url  = validators.url(vid_url)

    if form == "1":
        #CHECK URL VALIDATION
        if check_url == True:
            yt = YouTube(vid_url)
            stream = yt.streams.first()

            try:
                print(f"{bcolors.WARNING}================================================")
                print(f"{bcolors.WARNING}=  Script Created By SELF LEARNING (XxavianxX) =")
                print("================================================")
                print(f"{bcolors.WARNING}\n[+] DOWNLOADING THE VIDEO PLEASE WAIT ...")
                stream = yt.streams.first()
                stream.download("/home/xxavianxx/Desktop/")
                print(f"{bcolors.OKGREEN}[*] DOWNLOAD FINISHED !")
            except:
                print(f"{bcolors.FAIL}[!] ERROR ! TRY AGAIN")
                return
        else:
            print("INVALID URL !")
            return form
    elif form == "2":
        if check_url == True:
            yt = YouTube(vid_url)
            stream = yt.streams.first()
            try :
                print(f"{bcolors.WARNING}================================================")
                print(f"{bcolors.WARNING}=  Script Created By SELF LEARNING (XxavianxX) =")
                print(f"{bcolors.WARNING}================================================")
                print(f"{bcolors.WARNING}\n[+] DOWNLOADING THE VIDEO PLEASE WAIT ...")
                stream = yt.streams.filter(only_audio=True)
                stream[0].download()
                print(f"{bcolors.OKGREEN}[*] DOWNLOAD FINISHED !")
            except:
                print(f"{bcolors.FAIL}[!] ERROR ! TRY AGAIN")
                return
        else:
            print("INVALID URL !")
            return form
    elif form == "3":
        if check_url == True:
            yt = YouTube(vid_url)
            stream = yt.streams.first()
            try :
                print(f"{bcolors.WARNING}================================================")
                print(f"{bcolors.WARNING}=  Script Created By SELF LEARNING (XxavianxX) =")
                print(f"{bcolors.WARNING}================================================")
                print(f"{bcolors.WARNING}\n[+] DOWNLOADING THE PLAYLIST PLEASE WAIT ...")
                pl = Playlist(vid_url)
                pl.download_all("/home/xxavianxx/Desktop/")
                print(f"{bcolors.OKGREEN}[*] DOWNLOAD FINISHED !")
            except:
                print(f"{bcolors.FAIL}[!] ERROR ! TRY AGAIN")
                return
        else:
            print("INVALID URL !")
            return form

    else:
        print("INVALID CHOICE  !")
        exit()
Download()

