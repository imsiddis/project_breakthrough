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
import re
import json
import lxml
import urllib.request, json


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

get_now = get_price("span","em24 i")
get_avg = get_price("span","em24")


##############################################

#===========#
# Sørlandet #
# ==========# 

get_now = get_price("span","em24 i")
#get_avg = get_price("span","em24")
#get_min = get_price("span","em18")
get_max = get_price("","")

print(get_now)

#print(f"The electric price right now is {get_now} øre/kWh")
#print(f"The electric average price today is {get_avg} øre/kWh")
#print(f"The minimum price today is {get_min} øre/kWh")

