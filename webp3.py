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
from os.path import basename
import shutil
import glob



init()

FOLDER ='images/'

try:

    def run():
        
        web = "hc-security.com.mx"
        save = "final"
        
        welcome()
        folders()
        downloadweb(web,save)
        

    def downloadweb(web,save):

        console = Console()

        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        heraders = {'User-Agent': user_agent}
        
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

                #location = res["loc"]
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
        
        download_files(web,save)
                    
    def download_files(web,save):


        print(Fore.LIGHTRED_EX + "Searching Files in directory" + Fore.RESET)
        
        url = 'https://'+web
        response = urllib.request.urlopen(url)
        source =response.read()
        file = open(save+".txt", "wb")
        file.write(source)
        file.close()
        
        try:
            # make_directory()
            patten = '(http)?s:?(\/\/[^"]*\.(:png|jpg|jpeg|gif|png|svg|txt))'
            for line in open(save+".txt"):
                for m in re.findall(patten, line):
                    print('https: ' + m[1])
                    filename = basename(urllib.parse.urlsplit(m[1])[2])
                    print(filename)
                    request = 'https:' + urllib.parse.quote(m[1])
                    try:
                        img = urllib.request.urlopen(request).read()
                        file = open("images/"+filename, "wb")
                        file.write(img)
                        file.close()
                        print(Fore.GREEN + ">>>>>> Link Found with some images ....." + Fore.RESET)
                    except:
                        print(Fore.YELLOW + ">>>>>> With Invalid Characters" + Fore.RESET)
                        pass
                    break
        except AttributeError as ater:
            print(Fore.RED + "[+] Module Error \n")
            print(Fore.RED + ">>>>>> Proceso Detenito")
        except ModuleNotFoundError as moder:
            print(Fore.RED + "[+] Module not Found ", moder)
                    
    def folders():
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)  
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
