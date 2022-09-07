# in the name of God , Youtube Downloader Version = 1
from Downloader.Youtube import Youtube,ColorList
from random import choice
from re import match
from time import sleep
from datetime import date
from os import system,name

def Menu():
    Clear(0.5)
    PrintLow(f"""
{choice(ColorList)}$$$$          $$$$                  $$$             $$$
{choice(ColorList)} $$$$        $$$$                   $$$             $$$
{choice(ColorList)}  $$$$      $$$$                    $$$             $$$
{choice(ColorList)}   $$$$    $$$$                     $$$             $$$
{choice(ColorList)}    $$$$  $$$$                      $$$             $$$
{choice(ColorList)}     $$$$$$$$                       $$$             $$$
{choice(ColorList)}       $$$$           $$$$$$$       $$$             $$$
{choice(ColorList)}       $$$$        $$$       $$$    $$$             $$$
{choice(ColorList)}       $$$$       $$$         $$$   $$$             $$$
{choice(ColorList)}       $$$$         $$$      $$$      $$$$$$$$$$$$$$$
{choice(ColorList)}       $$$$           $$$$$$$           $$$$$$$$$$$
                {choice(ColorList)}{date.today()}


{choice(ColorList)}1 ) Downlaod Video
{choice(ColorList)}2 ) Download Music
{choice(ColorList)}3 ) Exit
    """,0.001)
    MenuCommand = input(f'\n{choice(ColorList)} ===>> ')
    if MenuCommand == '1':
        ChoiceOfQuality()
    elif MenuCommand == '2':
        GetLink('Music')
    elif MenuCommand == '3':
        Clear(0.5)
        PrintLow(f'{choice(ColorList)}God Bye :)',0.1)
        exit()
    else:
        PrintLow(f'{choice(ColorList)}Command Not Found',0.1)
        Clear(1)
        Menu()

def ChoiceOfQuality():
    Clear(1)
    PrintLow(f"""
                {choice(ColorList)}:: Choice Of Quality ::
    
{choice(ColorList)}1) High Quality
{choice(ColorList)}2) Low Quality
{choice(ColorList)}3) Back
{choice(ColorList)}4 ) Exit

    """,0.01)
    VideoPanelCommand = input(f'\n{choice(ColorList)} ===>> ')
    if VideoPanelCommand == '1':
        GetLink('VideoHigh')
    elif VideoPanelCommand == '2':
        GetLink('VideoLow')
    elif VideoPanelCommand == '3':
        PrintLow(f'{choice(ColorList)}Please Wait',0.1)
        Menu()
    elif VideoPanelCommand == '4':
        Clear(0.1)
        PrintLow(f'{choice(ColorList)}God Bye :)',0.1)
        exit()
    else:
        PrintLow(f'{choice(ColorList)}Command Not Found',0.5)
        ChoiceOfQuality()

def GetLink(Selection:str):
    Link = input(f'\n{choice(ColorList)} Give Link : ')
    Regex = match(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$",Link)
    if Regex:
        if Selection == 'VideoHigh':
            Clear(1)
            Status = Youtube(Link).VideoHight()
            DownloadCheck(Status)
        elif Selection == 'VideoLow':
            Clear(1)
            Status = Youtube(Link).VideoLow()
            DownloadCheck(Status)
        elif Selection == 'Music':
            Clear(1)
            Status = Youtube(Link).Music()
            DownloadCheck(Status)
        else:
            PrintLow(f'\n{choice(ColorList)}Error',0.1)
            DownloadCheck(Status)
    else:
        PrintLow(f'\n{choice(ColorList)}There is a Problem With The Link ',0.1)
        GetLink(Selection)

def PrintLow(Text:str,Time:float):
    for Char in Text:
        print(Char,end='',flush=True)
        sleep(Time)

def DownloadCheck(Value):
    if Value:
        PrintLow(f'\n{choice(ColorList)}The Download is Done :)',0.1)
        Menu()
    else:
        PrintLow(f'\n{choice(ColorList)}Download Failed :(',0.1)
        Menu()

def Clear(Time:float):
    sleep(Time)
    system('clear' if name == 'posix' else 'cls')

if __name__ == '__main__':
    Menu()