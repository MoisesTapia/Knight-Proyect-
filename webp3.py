#!/usr/bin/python
# Author: Moises Tapia
# Dart - Security

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
import nmap
import time

init()

FOLDER ='images/'

try:

    def run():
        
        web = "hc-security.com.mx"
        save = "Testing"
        
        authors_welcome()
        welcome_infoghatering()
        folders()
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

                #ip_priv = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
                
                print("\n" + Fore.LIGHTYELLOW_EX + " [+] Info network" + Fore.RESET)
                datos = [["ip_priv",ip_pub,gethostby_,]]
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
                        print(Fore.GREEN + " [+] Link Found with some images ....." + Fore.RESET)
                    except:
                        print(Fore.YELLOW + " [+] With Invalid Characters" + Fore.RESET)
                        pass
                    break
        except AttributeError as ater:
            print(Fore.RED + "[+] Module Error \n")
            print(Fore.RED + " [+] Proceso Detenito")
        except ModuleNotFoundError as moder:
            print(Fore.RED + "[+] Module not Found ", moder)

    def port_scann(web):


        nm = nmap.PortScanner()
        gethostby_ = socket.gethostbyname(web)

        portlist=" 1,21,22,23,53,80,110,135,139,143,8080,443,389,445,591,993,995,2086,3389,3306,3128,3030,9898,10000,19226,12345,31337" # 21,22,23,135,139,80,8080,443
        nm.scan(hosts=web,arguments='-T3 -n -Pn -p' + portlist)

        
        host_list =[(x,nm[x]['status']['state']) for x in nm.all_hosts()]

        file = open('scan.txt','w')
        for hosts,status in host_list:
            print (hosts,status)
            file.write(hosts+'\n')

        array_porlist=portlist.split(',')
        for port in array_porlist:
            state= nm[gethostby_]['tcp'][int(port)]['state']
            if state == "open":

                print (Fore.LIGHTCYAN_EX+"[ ✔ ] Open Port: "+str(port)+"  "+" state: " + state + Fore.RESET)
                file.write("Port: "+str(port)+" state: "+state+ "\n")
        file.close()
    def port_scann(web):

        nm = nmap.PortScanner()
        gethostby_ = socket.gethostbyname(web)

        portlist=" 1,21,22,23,53,80,110,135,139,143,8080,443,389,445,591,993,995,2086,3389,3306,3128,3030,9898,10000,19226,12345,31337" # 21,22,23,135,139,80,8080,443
        nm.scan(hosts=web,arguments='-T3 -n -Pn -p' + portlist)

        
        host_list =[(x,nm[x]['status']['state']) for x in nm.all_hosts()]

        file = open('scan.txt','w')
        for hosts,status in host_list:
            print (hosts,status)
            file.write(hosts+'\n')

        array_porlist=portlist.split(',')
        for port in array_porlist:
            state= nm[gethostby_]['tcp'][int(port)]['state']
            if state == "open":

                print (Fore.LIGHTCYAN_EX+"[ ✔ ] Open Port: "+str(port)+"  "+" state: " + state + Fore.RESET)
                file.write("Port: "+str(port)+" state: "+state+ "\n")
        file.close()
    def folders():
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)  
    def welcome_infoghatering():
        tprint('''
        Web
        Information
        Gathering''', decoration="barcode1") # , font="random-small"
        art_0 = art("coffe")
        print(art_0 + Fore.LIGHTYELLOW_EX +" By: Equinockx" + Fore.RESET + "\n")

    def authors_welcome():

        console = Console()
        tprint("Knight - Proyect")
        print(Fore.LIGHTCYAN_EX+''' 
                          (O)
                      <M
           o          <M  Dart - Security!!!
          /| ......  /:M\------------------------------------------------,,,,,,
        (O)[]XXXXXX[]I:K+}=====<{H}>================================------------>
          \| ^^^^^^  \:W/------------------------------------------------\''\'\'''
           o          <W  Information Gathering
                      <W
                      (O)
        '''+Fore.RESET)
        art_0 = art("coffe")
        print("\n"+art_0 + Fore.LIGHTYELLOW_EX +" By: Equinockx " + Fore.RESET + Fore.LIGHTGREEN_EX + "- Dart-Security " + Fore.RESET + Fore.LIGHTBLUE_EX + "- Adan Vazquez " + Fore.RESET + "\n")
        authors = Table(show_header=True, header_style="bold green")
        authors.add_column("Name", style="dim", justify="center")
        authors.add_column("Github", style="dim", justify="center")
        authors.add_column("Page", style="dim", justify="center")
        authors.add_row(
            "Moises Tapia",
            "[yellow]https://github.com/MoisesTapia[/yellow]",
            "[underline]hc-security.com.mx[/underline]"
        )
        authors.add_row(
            "Dart - Security",
            "[green]https://github.com/dart-security[/green]",
            "[underline]hc-security.com.mx[/underline]"
        )
        authors.add_row(
            "Adan Vazquez",
            "[blue]https://github.com/AdanOSwin[/blue]",
            "[underline]hc-security.com.mx[/underline]"
        )
        console.print(authors)
        time.sleep(5)
        os.system ("clear")

    run()
except KeyboardInterrupt as kbi:
    print(Fore.RED + "\n Programa interrumpido por el usuario ...." + Fore.RESET)
