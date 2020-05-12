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

def welcome():

        console = Console()

        tprint("Dart - Security", decoration="barcode1")
        art_0 = art("coffe")
        print(art_0 + Fore.LIGHTYELLOW_EX +" By: Equinockx" + Fore.RESET + "\n")

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

        console.print(authors)

run()
