#!/usr/bin/python
# Author: Moises Tapia

from art import *
import urllib.request
from colorama import Fore, init, Back, Style
import urllib.parse
import re
from rich.console import Console
from rich.table import Column, Table
import os
import requests
import socket
import json


init()

try:

    def run():
        welcome()
        downloadweb()

    def downloadweb():

        console = Console()

        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        heraders = {'User-Agent': user_agent}
        
        web = "hc-security.com.mx"
        save = "final"
        #web = input(Fore.LIGHTBLUE_EX + "[*] Enter your web: \n >> " + Fore.RESET)
        #save = input(Fore.YELLOW + "[*] Name of your safe file: " + Fore.RESET)
        request = urllib.request.Request("https://" + web, headers=heraders)
        
        with urllib.request.urlopen(request) as response:
            with open(save+".html", "wb") as out:
                out.write(response.read())

                
                print(Fore.GREEN + ">>> Page Downloaded ..." + Fore.RESET)
                folder= os.path.dirname(os.path.abspath(save))
                print(Fore.YELLOW + ">>> Resume ..." + Fore.RESET)
                #Resume
                resume = Table(show_header=True, header_style="bold red")
                resume.add_column("Web", style="dim", justify="center")
                resume.add_column("Url", style="dim", justify="center")
                resume.add_column("File", style="dim", justify="center")
                resume.add_column("Location", style="dim", justify="center")

                resume.add_row(
                    web,
                    "https://"+web,
                    save+".html",
                    folder

                )
            
                console.print(resume)


                gethostby_ = socket.gethostbyname(web)
                info_2=requests.get("https://ipinfo.io/"+gethostby_+"/json")
                res = json.loads(info_2.text)

                location = res["loc"]
                reg = res["region"]
                city = res["city"]
                country = res["country"]


                print(Fore.LIGHTBLUE_EX + " >>> Target Information...." + Fore.RESET)

                location = Table(show_header=True, header_style="bold red")
                location.add_column("IP", style="dim", justify="center")
                #location.add_column("Location", style="dim", justify="center")
                location.add_column("Region", style="dim", justify="center")
                location.add_column("City", style="dim", justify="center")
                location.add_column("Country", style="dim", justify="center")
                
                location.add_row(
                    gethostby_,
                    reg,
                    city,
                    country
                )
                
                console.print(location)

                print(Fore.LIGHTBLUE_EX + " >>> More Details...." + Fore.RESET)
                dom = requests.get("\nhttps://"+ web)
                dic = dom.headers
                for date,key in dic.items():
                    print("|",date,"|",key,"|")


    def welcome():
        tprint('''
        Web
        Information
        Gathering''', decoration="barcode1") # , font="random-small"
        art_0 = art("coffe")
        print(art_0 + Fore.LIGHTYELLOW_EX +" By: Equinockx" + Fore.RESET + "\n")
        
    def public_ip():
    
         my_ip= urllib.request.urlopen("https://checkip.dyndns.org").read
         lis = "0123456789."
         ip = ""
         for x in str(dato):
             if x in lis:
                 ip += x
         return ip
    
    run()
except KeyboardInterrupt as kbi:
    print(Fore.RED + "\n Programa interrumpido por el usuario ...." + Fore.RESET)
