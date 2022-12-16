# This program will check what the current price of electricity is in your area. (Norway Only)
#=======================================================#
# Target:                                               #
# https://www.lyse.no/strom/strompriser?postnummer=4009 #
#=======================================================#

#==============================#
# Import the necessary modules #
#==============================#
import requests
import bs4

# Get the electricity price from "https://www.lyse.no/strom/strompriser?postnummer=4009"
def get_price(postnummer):
    # First, we will get the HTML of the page.
    page = requests.get(f"https://www.lyse.no/strom/strompriser?postnummer={postnummer}")
    # Then we will parse the HTML using beautifulsoup.
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    # Now we will find the price of electricity.
    price = soup.find("h1", "class=StyledHeading-sc-1rdh4aw-0 gUkQjO sc-93d72a4f-0 hJtcJS")
    # We will now return the price.
    return price

# Request postal code from user.
def get_postal_code():
    postal_code = input("Enter your postal code: ")
    return postal_code

def main():
    # Get the postal code from the user.
    postnummer = get_postal_code()
    # Get the price of electricity.
    price = get_price(postnummer)
    # Print the price of electricity.
    print(price)

main()
