# This program should request a URL from the user, then scrape the email addresses from the page and print them to the screen.
# Author: imSiddis

import re
import urllib.request

def getURL():
    url = input("Enter a URL: ")
    return url

def getHTML(url):
    html = urllib.request.urlopen(url).read() # This will read the HTML from the URL
    return html

def getEmails(html):
    email_list = []
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', str(html)) # This regex will find all email addresses on the page
    email_list.append(emails)
    return email_list

# This function removes duplicates from the list returned by getEmails()
# It will use a set to remove duplicates, then convert the set back to a list
def removeDuplicates(emails):
    email_list = []
    for email in emails:
        no_duplicates = list(set(email)) # This will remove duplicates from the list
        for i in no_duplicates:
            email_list.append(i)
        return email_list # This will return the list without duplicates

def printEmails(emails):
    for email in emails:
        print(email)

# A function to append the non-duplicate emails to a file.
def saveEmails(emails):
    with open("emails.txt", "a") as file:
        for email in emails:
            file.write(email + "\n")

# A menu function to allow the user to choose what they want to do with the emails
def menu(emails):
    print("What would you like to do with the emails?")
    print("1. Print emails to screen")
    print("2. Save emails to file")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        printEmails(emails)
    elif choice == "2":
        saveEmails(emails)
    elif choice == "0":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice")
        menu(emails)

def main():
    # Splash screen
    print("================== MailScrape v1.0 ========================")
    print("|                   By imSiddis                            |")
    print("============================================================")
    print("| This program will scrape email addresses from a website. |")
    print("============================================================")
    url = getURL()
    html = getHTML(url)
    emails = getEmails(html)
    no_duplicates = removeDuplicates(emails)
    sorted_emails = sorted(no_duplicates)
    printEmails(sorted_emails) 

main()