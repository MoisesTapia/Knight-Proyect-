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
import socket
import requests
from requests import get
from socket import AF_INET, SOCK_STREAM
import json
from os.path import basename
import shutil
import glob
import publicip
import netifaces as ni


init()
FOLDER = "images/"
try:

    def run():
        welcome()
        folders()
        
        web = input(Fore.LIGHTBLUE_EX + "[*] Enter your web: \n >> " + Fore.RESET)
        save = input(Fore.YELLOW + "[*] Name of your safe file: " + Fore.RESET)
        
        downloadweb(web,save)
        port_scann(web)

    def downloadweb(web,save):

        console = Console()

        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        heraders = {'User-Agent': user_agent}
        
        request = urllib.request.Request("https://" + web, headers=heraders)
        
        with urllib.request.urlopen(request) as response:
            with open(save+".html", "wb") as out:
                out.write(response.read())

                
                print(Fore.GREEN + " [+] Page Downloaded ..." + Fore.RESET)
                folder= os.path.dirname(os.path.abspath(save))
                print(Fore.YELLOW + " [+] Resume ..." + Fore.RESET)
                # ---------------------------------------------------------------------
                resume = Table(show_header=True, header_style="bold red")
                resume.add_column("Web", style="dim", justify="center")
                resume.add_column("Url", style="dim", justify="center")

                resume.add_row(
                    web,
                    "https://"+web,
                )
            
                console.print(resume)

                # ---------------------------------------------------------------------
                gethostby_ = socket.gethostbyname(web)
                info_2=requests.get("https://ipinfo.io/"+gethostby_+"/json")
                res = json.loads(info_2.text)

                reg = res["region"]
                city = res["city"]
                country = res["country"]
                
                print(Fore.LIGHTBLUE_EX + " [+] Target Information...." + Fore.RESET)

                location = Table(show_header=True, header_style="bold red")
                location.add_column("File html", style="dim", justify="center")
                location.add_column("File.txt", style="dim", justify="center")
                location.add_column("Location", style="dim", justify="center")
                
                location.add_row(
                    save+".html",
                    save+".txt",
                    folder,
                )
                
                console.print(location)
                # -----------------------------------------------------------------------
                print(Fore.LIGHTBLUE_EX + " [+] Target Information...." + Fore.RESET)

                savein = Table(show_header=True, header_style="bold red")
                savein.add_column("Region", style="dim", justify="center")
                savein.add_column("City", style="dim", justify="center")
                savein.add_column("Country", style="dim", justify="center")

                savein.add_row(
                    reg,
                    city,
                    country, 
                )
                
                console.print(savein)
                # ------------------------------------------------------------------------
                ip_pub =get("https://api.ipify.org").text

                ip_priv = ni.ifaddresses('eth1')[ni.AF_INET][0]['addr']
                
                print("\n" + Fore.LIGHTYELLOW_EX + " [+] Info network" + Fore.RESET)
                datos = [[ip_priv,ip_pub,gethostby_,]]
                detalles ='''\
                ----------------------------------------------------
                |   Private(src)  |   Public       |   Web(dst)    |
                ----------------------------------------------------
                | {}                                                                      
                |---------------------------------------------------\
                '''
                details = (detalles.format("\n".join(" {:<8}     {:<10}    {:>8}".format(*fila)for fila in datos)))
                print(Fore.LIGHTMAGENTA_EX + details + Fore.RESET)
                # ---------------------------------------------------------------------------------------------------
                print(Fore.LIGHTBLUE_EX + " >>> More Details...." + Fore.RESET)
                dom = requests.get("\nhttps://"+ web)
                dic = dom.headers
                for date,key in dic.items():
                    print("|",date,"|",key,"|")
                # ---------------------------------------------------------------------------------------------------
        download_files(web,save)
                    
    def download_files(web,save):


        print("\n" + Fore.LIGHTMAGENTA_EX + "Searching Files in directory" + Fore.RESET)
        
        url = 'https://'+web
        response = urllib.request.urlopen(url)
        source =response.read()
        file = open(save+".txt", "wb")
        file.write(source)
        file.close()
        
        try:
            
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
                        print(Fore.GREEN + " [ ✔ ] Link Found with some images ....." + Fore.RESET)
                    except:
                        print(Fore.YELLOW + " [ ~ ] With Invalid Characters" + Fore.RESET)
                        pass
                    break
        except AttributeError as ater:
            print(Fore.RED + "[+] Module Error \n")
            print(Fore.RED + " [+] Proceso Detenito")
        except ModuleNotFoundError as moder:
            print(Fore.RED + "[+] Module not Found ", moder)

    def port_scann(web):

        start = 1
        end = 6000
        ip = socket.gethostbyname(web)
        print("\n" + Fore.LIGHTBLUE_EX+"[>>>>>] Starting Scanning: ", ip +Fore.RESET+ "\n")

        for port in range(start,end):
            s = socket.socket(AF_INET,SOCK_STREAM)
            s.settimeout(5)
            if(s.connect_ex((ip,port))==0):
                print("\033[1;32m"+"[ ✔ ] Open Port " + str(port) + "\033[0;m")
                status = "[ ✔ ] Open port: " + str(port)
                file = open("ports.txt", "a")
                file.write(str(status) + os.linesep)
                file.close()
            s.close()

        print("\n"+Fore.LIGHTCYAN_EX+"[<<<<<] Scanning is Done.... and scann saved" + Fore.RESET)

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
    
    #def find_email():
    
    run()
except KeyboardInterrupt as kbi:
    print(Fore.RED + "\n Programa interrumpido por el usuario ...." + Fore.RESET)
