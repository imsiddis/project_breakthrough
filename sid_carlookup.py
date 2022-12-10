# This program will use the API for "veivesenet.no" to lookup a car by its registration number.
# Author: imSiddis

import requests


def getReg():
    reg = input("Enter a registration number: ")
    return reg

def getCar(reg):
    url = "https://veivesenet.no/api/vehicle/" + reg
    response = requests.get(url)
    data = response.json()
    return data

def printCar(data):
    print("Brand: " + data["brand"])
    print("Model: " + data["model"])
    print("Year: " + data["year"])
    print("Fuel: " + data["fuel"])
    print("Engine: " + data["engine"])
    print("Weight: " + data["weight"])
    print("Color: " + data["color"])
    print("Type: " + data["type"])


def main():
    # Splash screen
    print("This program will use the API for \"veivesenet.no\" to lookup a car by its registration number.")
    print("Author: imSiddis")
    print(" ")
    reg = getReg()
    data = getCar(reg)
    printCar(data)

main()

