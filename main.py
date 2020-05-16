#!/usr/bin/python

from rich.console import Console
from rich.table import Column, Table
from colorama import Fore, init, Back, Style
from art import *
import os


init()

def run():
    
    welcome()
    menu()

def menu():
    

    console = Console()

    options = Table(show_header=True, header_style="bold green")
    options.add_column("Number", style="dim", justify="center")
    options.add_column("Option", style="dim", justify="center")
    options.add_row(
        "1",
        "[cyan]Network Menu[/cyan]"
    )
    options.add_row(
        "2",
        "[cyan]Web Menu[/cyan]"
    )
    
    console.print(options)
    
    try:
        preg = True     
        while preg:

            opc = input(Fore.LIGHTMAGENTA_EX + " >>  " + Fore.RESET )
            opc = int(opc)

            if opc == 1:
                print(Fore.LIGHTRED_EX + "Modulo en Desarrollo" + Fore.RESET)
                preg == False
            elif opc == 2:
                os.system("python3 download_web3.py")
                # print(Fore.LIGHTRED_EX + "Modulo en Desarrollo" + Fore.RESET)
                preg == False
            else:
                print(Fore.LIGHTRED_EX + "Opcion no encontrada" + Fore.RESET)
    except KeyboardInterrupt as ky:
        print(Fore.LIGHTCYAN_EX + f"\n\nInterrumpido por el usuario...{ky}" + Fore.RESET)
            
            
def welcome():
    
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

run()
