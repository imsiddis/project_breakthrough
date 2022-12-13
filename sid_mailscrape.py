# This program should request a URL from the user, then scrape the email addresses from the page and print them to the screen.
# Author: imSiddis

import re
import urllib.request



def getURL():
    url = input("Enter a URL: ")
    if url.startswith("http://") or url.startswith("https://"):
        pass
    elif not url.startswith("http://") or not url.startswith("https://"): # This will check if the URL starts with http:// or https://
        url = "https://" + url # If it doesn't, it will add http:// to the start of the URL
    return url

def getHTML(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}) # This will add a user-agent to the request
    html = urllib.request.urlopen(req).read() # This will read the HTML from the URL
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

# A function that will remove emails not ending with TDL like .com, .net, .org, etc.
def removeInvalidEmails(emails):
    # email_endwith = [Country TDLs]
    email_endwith = [".no",".com",".uk",".to",".net",".gov",".org",".edu",".mil",".int",".arpa",".biz",".aero",".coop",".info",".name",".pro",".museum",".coop",".travel",".mobi",".cat",".jobs",".tel",".asia",".post",".xxx",".edu",".gov",".mil",".net",".org",".biz",".info",".name",".pro",".aero",".coop",".museum",".int",".travel",".post",".jobs",".mobi",".tel",".xxx",".ac",".ad",".ae",".af",".ag",".ai",".al",".am",".an",".ao",".aq",".ar",".as",".at",".au",".aw",".az",".ba",".bb",".bd",".be",".bf",".bg",".bh",".bi",".bj",".bm",".bn",".bo",".br",".bs",".bt",".bv",".bw",".by",".bz",".ca",".cc",".cd",".cf",".cg",".ch",".ci",".ck",".cl",".cm",".cn",".co",".cr",".cu",".cv",".cx",".cy",".cz",".de",".dj",".dk",".dm",".do",".dz",".ec",".ee",".eg",".eh",".er",".es",".et",".fi",".fj",".fk",".fm",".fo",".fr",".ga",".gb",".gd",".ge",".gf",".gg",".gh",".gi",".gl",".gm",".gn",".gp",".gq",".gr",".gs",".gt",".gu",".gw",".gy",".hk",".hm",".hn",".hr",".ht",".hu",".id",".ie",".il",".im",".in",".io",".iq",".ir",".is",".it",".je",".jm",".jo",".jp",".ke",".kg",".kh",".ki",".km",".kn",".kp",".kr",".kw",".ky",".kz","."]
    valid_emails = []
    for email in emails:
        for i in email_endwith:
            if email.endswith(i):
                valid_emails.append(email)
    return valid_emails

def printEmails(emails):
    print("=========================================")
    print("|    ~~ Emails found on the page ~~     |")
    print("=========================================")
    for email in emails:
        print(email)
    print("=========================================")
    print("          ~~ End of emails ~~           ")
    print("     \tTotal emails found: " + str(len(emails)))
    print("=========================================")

# A function to append the non-duplicate emails to a file.
def saveEmails(emails):
    with open("emails.txt", "a") as file: 
        for email in emails:
            file.write(email + "\n")

# This function will print the program's information
def about():
    print("===================== MailScrape v1.0 ======================")
    print("|                      by imSiddis.                        |")
    print("============================================================")
    print("| This program will scrape email addresses from a website. |")
    print("| It will then print them to the screen or save them to a  |")
    print("| file.                                                    |")
    print("============================================================")

# A menu function to allow the user to choose what they want to do with the emails
# This menu should be called before the emails have been scraped and sorted.

def menu(emails):
    print("===================== MailScrape v1.0 ======================")
    print("|                      By imSiddis                         |")
    print("============================================================")
    print("| This program will scrape email addresses from a website. |")
    print("============================================================")
    print("What would you like to do with the emails?")
    print("1. Print emails to screen")
    print("2. Save emails to file")
    print("3. About")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        url = getURL()
        html = getHTML(url)
        emails = getEmails(html)
        no_duplicates = removeDuplicates(emails)
        sorted_emails = sorted(no_duplicates)
        printEmails(sorted_emails)
        input("Press enter to return to the menu") # This will pause the program until the user presses enter
        menu(emails)
        
    elif choice == "2":
        url = getURL()
        html = getHTML(url)
        emails = getEmails(html)
        no_duplicates = removeDuplicates(emails)
        sorted_emails = sorted(no_duplicates)
        saveEmails(sorted_emails)
    
    elif choice == "3":
        about()
        input("Press enter to return to the menu") # This will pause the program until the user presses enter
        print("\n\n\n\n\n\n")
        menu(emails)
    elif choice == "0":
        confirmExit()
    else:
        print("Invalid choice")
        menu(emails)

# def main():
#     # Splash screen
#     print("===================== MailScrape v1.0 ======================")
#     print("|                      By imSiddis                         |")
#     print("============================================================")
#     print("| This program will scrape email addresses from a website. |")
#     print("============================================================")
#     # Main program
#     url = getURL()
#     html = getHTML(url)
#     emails = getEmails(html)
#     no_duplicates = removeDuplicates(emails)
#     sorted_emails = sorted(no_duplicates)
#     menu(sorted_emails)

# Confirm exit
def confirmExit():
    print("Are you sure you want to exit? (Y/n)") # Ask the user if they want to exit
    choice = input("Enter your choice: ")
    if choice == "Y" or choice == "y" or choice == "":
        print("Exiting...")
        exit()
    elif choice == "N" or choice == "n":
        menu(emails=getURL)
    else:
        print("Invalid choice")
        confirmExit()

menu(getURL)