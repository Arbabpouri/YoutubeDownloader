# in the name of God , Youtube Downloader Version = 1
from pytube import YouTube
from random import choice
from colorama import Fore
from os import path,makedirs
ColorList = [Fore.GREEN,Fore.LIGHTGREEN_EX,Fore.BLUE,Fore.CYAN,Fore.YELLOW,Fore.MAGENTA,Fore.RED,Fore.LIGHTWHITE_EX,Fore.WHITE,Fore.LIGHTRED_EX,Fore.LIGHTCYAN_EX,Fore.LIGHTYELLOW_EX,Fore.LIGHTMAGENTA_EX]
if not path.exists("Video"):
    makedirs("Video")
if not path.exists("Music"):
    makedirs("Music")
class Youtube(object):
    def __init__(self,Link) -> None:
        self.Link = Link
    def VideoHight(self):
        try:
            print(f'{choice(ColorList)}Connect To {choice(ColorList)}Youtube')
            Connect = YouTube(self.Link)
            print(f'{choice(ColorList)}Download . . .')
            Download = Connect.streams.get_highest_resolution().download('Video')
            return True
        except:
            return False
    def VideoLow(self):
        try:
            print(f'{choice(ColorList)}Connect To {choice(ColorList)}Youtube')
            Connect = YouTube(self.Link)
            print(f'{choice(ColorList)}Download . . .')
            Download = Connect.streams.get_lowest_resolution().download('Video')
            return True
        except:
            return False
    def Music(self):
        try:
            print(f'{choice(ColorList)}Connect To {choice(ColorList)}Youtube')
            Connect = YouTube(self.Link)
            print(f'{choice(ColorList)}Download . . .')
            Download = Connect.streams.get_audio_only().download('Music')
            return True
        except:
            return False