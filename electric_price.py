# This program will check what the current price of electricity is in your area. (Norway Only)
#=======================================================#
# Target:                                               #
# https://www.lyse.no/strom/strompriser?postnummer=4009 #
#=======================================================#

#==========================================#
# New target:                              #
# https://polarkraft.no/dagens-timepriser/ #
#==========================================#


#==============================#
# Import the necessary modules #
#==============================#
import requests
import bs4
import os
import datetime


# Get the electricity price from "https://www.lyse.no/strom/strompriser?postnummer=4009"

def get_price(t1, t2):
    # First, we will get the HTML of the page.
    page = requests.get(f"https://minspotpris.no/")
    # Then we will parse the HTML using beautifulsoup.
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    # Now we will find the price of electricity.
    element = soup.find(t1, class_=t2)
    price = element.get_text()


    # We will now return the price.    
    return price

##############################################

#===========#
# Sørlandet #
# ==========# 
def sørlandet():
    clear_screen()
    print("#=========================#")
    print("# Valgt område: Sørlandet #")
    print("#=========================#")
    print("# 1. Pris nå              #")
    print("# 2. Snittpris i dag      #")
    print("# 3. Minimumspris i dag   #")
    print("# 4. Maksimumspris i dag  #")
    print("# 5. Full oversikt        #")
    print("# 0. Tilbake              #")
    print("#=========================#")
    valg = input("Valg: ")
    if valg == "1":
        get_now = get_price("span","em24 i")
        print(f"Prisen nå er {get_now} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        sørlandet()
    elif valg == "2":
        get_avg = get_price("span","em24")
        print(f"Snittprisen i dag er {get_avg} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        sørlandet()
    elif valg == "3":
        get_min = get_price("span","em18")
        print(f"Minimumsprisen i dag er {get_min} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        sørlandet()
    elif valg == "4":
        get_max = get_price("span","em18")
        print(f"Maksimumsprisen i dag er {get_max} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        sørlandet()
    elif valg == "5":
        clear_screen()
        # Date should be formatted like this: DD/MM/YYYY
        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y")
        get_now = get_price("span","em24 i")
        get_avg = get_price("span","em24")
        get_min = get_price("span","em18")
        get_max = get_price("span","em18")
        print("#=========================================#")
        print("#               Full oversikt             #")
        print("#=========================================#")
        print(f"# Dato: {date}")
        print(f"# Prisen nå er {get_now} øre/kWh")
        print(f"# Snittprisen i dag er {get_avg} øre/kWh")
        print(f"# Minimumsprisen i dag er {get_min} øre/kWh")
        print(f"# Maksimumsprisen i dag er {get_max} øre/kWh")
        print("#=========================================#")
        print("")
        print("Trykk enter for å fortsette...")
        input()
        sørlandet()
        
    elif valg == "0":
        electric_menu()
        sørlandet()
    else:
        print("Ugyldig valg!")
        sørlandet()


#==============================#
#      ~~ Electric Menu ~~     #
#==============================#
def menu_banner():
    clear_screen()
    print("#======================================#")
    print("#        ~~ Strømpris Meny ~~          #")
    print("#======================================#")
    print("# 1. Sørlandet                         #")
    print("# 2. Vestlandet (Kommer snart)         #")
    print("# 3. Trøndelag (Kommer snart)          #")
    print("# 4. Nord-Norge (Kommer snart)         #")
    print("# 5. Midt-Norge (Kommer snart)         #")
    print("# 6. Østlandet (Kommer snart)          #")
    print("# 7. Om programmet                     #")
    print("# 0. Avslutt                           #")
    print("#======================================#")

def about():
    clear_screen()
    print("#=============================================================#")
    print("# Strømpris v1.0 (Beta) (c) 2021 imSiddis                     #")
    print("#=============================================================#")
    print("# Dette programmet er laget av imSiddis                       #")
    print("# Programmet er laget for å sjekke strømprisen i ditt område. #")
    print("# Data er hentet fra: https://minspotpris.no/                 #")
    print("#=============================================================#")
    print("~ Trykk enter for å fortsette... ~")
    input()
    electric_menu()

def electric_menu():
    menu_banner() # Print the menu banner
    menu_choice = input("Velg et alternativ: ") # Get the user input
    if menu_choice == "1":
        print("Sørlandet")
        sørlandet()
    elif menu_choice == "2":
        print("Vestlandet")
    elif menu_choice == "3":
        print("Trøndelag")
    elif menu_choice == "4":
        print("Nord-Norge")
    elif menu_choice == "5":
        print("Midt-Norge")
    elif menu_choice == "6":
        print("Østlandet")
    elif menu_choice == "7":
        about()
    elif menu_choice == "0":
        confirm_exit()
    else:
        print("Ugyldig valg!")
        electric_menu()

def confirm_exit():
    clear_screen()
    print("Er du sikker på at du vil avslutte? (Y/n)")
    confirm = input("Valg: ")
    if confirm == "Y" or confirm == "y" or confirm == "":
        print("Avslutter...")
        exit()
    elif confirm == "N" or confirm == "n":
        electric_menu()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def start():
    electric_menu()

start()
