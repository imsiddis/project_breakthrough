# This program will check what the current price of electricity is in your area. (Norway Only)
# This program is made by: imSiddis
#==============================#
# Import the necessary modules #
#==============================#
import requests
import bs4
import os
import datetime
import time

#=======================#
# Build version of code #
#=======================#
build_version = "0.5 (Beta)"

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
#===============================================#
# Date should be formatted like this: DD/MM/YYYY
date = datetime.datetime.now()
date = date.strftime("%d/%m/%Y")
# Clock should be formatted like this: HH:MM:SS #
clock = datetime.datetime.now()
clock = clock.strftime("%H:%M:%S")
#===============================================#
#============#
# Vestlandet # 
#============# 
def vestland():
    clear_screen()
    print("#========================#")
    print("# ~ Hva vil du sjekke? ~ #")
    print("#========================#")
    print("# 1. Pris nå             #")
    print("# 2. Snittpris i dag     #")
    print("# 3. Minimumspris i dag  #")
    print("# 4. Maksimumspris i dag #")
    print("# 5. Full oversikt       #")
    print("# 6. Oversikt imorgen    #")
    print("# 0. Tilbake             #")
    print("#========================#")
    valg = input("Valg: ")
    if valg == "1":
        loading()
        get_now = get_price("span","em24 i")
        print(f"Prisen nå er {get_now} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        vestland()
    elif valg == "2":
        loading()
        get_avg = get_price("span","em24")
        print(f"Snittprisen i dag er {get_avg} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        vestland()
    elif valg == "3":
        loading()
        get_min = get_price("span","em18")
        print(f"Minimumsprisen i dag er {get_min} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        vestland()
    elif valg == "4":
        loading()
        get_max = get_price("td","r red")
        print(f"Maksimumsprisen i dag er {get_max} øre/kWh")
        print("Trykk enter for å fortsette...")
        input()
        vestland()
    elif valg == "5":
        get_now = get_price("span","em24 i")
        get_avg = get_price("span","em24")
        loading()
        get_min = get_price("span","em18")

        # get_max should look for the next span element with the class "em18" after the first one.
        get_max = get_price("td","r red")
        
        clear_screen()
        print("#=============================================#")
        print("#               ~ Full oversikt ~             #")
        print("#=============================================#")
        print(f"# Tidspunkt: {clock}                         #")
        print(f"# Dato: [{date}]                          #")
        print("#=============================================#")
        print(f"# Prisen nå er {get_now} øre/kWh                 #")
        print(f"# Snittprisen i dag er {get_avg} øre/kWh         #")
        print(f"# Minimumsprisen i dag er {get_min} øre/kWh      #")
        print(f"# Maksimumsprisen i dag er {get_max} øre/kWh #")
        print("#=============================================#")
        print("")
        print("     ~ Trykk enter for å fortsette ~")
        input()
        vestland()
    elif valg == "6":
        try:
            tomorrow_avg = get_price("span","em24 c")
            tomorrow_min = get_price("span","em24 c green")
            loading()
            tomorrow_max = get_price("span","em24 c red")
            clear_screen()
            print("#===========================================#")
            print("#                Full oversikt              #")
            print("#===========================================#")
            print(f"# For imorgen [{date}]:                 #")
            print("#===========================================#")
            print(f"# Snittprisen imorgen er {tomorrow_avg} øre/kWh")
            print(f"# Minimumsprisen imorgen er {tomorrow_min} øre/kWh")
            print(f"# Maksimumsprisen imorgen er {tomorrow_max} øre/kWh")
            print("#===========================================#")
            print("")
            print("      ~ Trykk enter for å fortsette ~ ")
            input()
            vestland()
        except:
            clear_screen()
            print("#==================================================================#")
            print("# Det er ingen oversikt for imorgen på dette tidspunktet.          #")
            print("# Morgendagens oversikt blir lagt ut kl. 14:00 hver dag.           #")
            print("# Prøv igjen senere.                                               #")
            print("#==================================================================#")
            print("              ~ Trykk enter for å fortsette ~")
            input()
            vestland()
    elif valg == "0":
        electric_menu()
        vestland()
    else:
        print("Ugyldig valg!")
        vestland()


#==============================#
#      ~~ Electric Menu ~~     #
#==============================#
def menu_banner():
    clear_screen()
    print("#======================================#")
    print("#        ~~ Strømpris Meny ~~          #")
    print("#======================================#")
    print("# 1. Sjekk Strømpris                   #")
    print("# 2. Om programmet                     #")
    print("# 0. Avslutt                           #")
    print("#======================================#")

def about():
    clear_screen()
    print("#=============================================================#")
    print(f"# Strømpris v{build_version} ~ 2022 imSiddis                       #")
    print("#=============================================================#")
    print("# Dette programmet er laget av imSiddis                       #")
    print("# Programmet er laget for å sjekke strømprisen i ditt område. #")
    print("# Data hentes fra: https://minspotpris.no/                    #")
    print("# Strømprisen vil variere fra hvor din IP address kommer fra. #")
    print("#=============================================================#")
    print("# My github: https://github.com/imsiddis/                     #")
    print("#=============================================================#")
    print("              ~ Trykk enter for å fortsette ~")
    input()
    electric_menu()

def electric_menu():
    menu_banner() # Print the menu banner
    menu_choice = input("Velg et alternativ: ") # Get the user input
    if menu_choice == "1":
        print("Sørlandet")
        vestland()
    elif menu_choice == "2":
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

# Animated loading screen
def loading():
    for i in range(0, 3):
        print("Laster inn...")
        time.sleep(0.1)
        clear_screen()
        print("Laster inn..")
        time.sleep(0.1)
        clear_screen()
        print("Laster inn.")
        time.sleep(0.1)
        clear_screen()

def start():
    electric_menu()

start()