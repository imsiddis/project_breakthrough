# This program should request a URL from the user, then scrape the email addresses from the page and print them to the screen.
# Author: imSiddis

import re
import urllib.request

def getURL():
    url = input("Enter a URL: ")
    return url

def getHTML(url):
    html = urllib.request.urlopen(url).read()
    return html

def getEmails(html):
    email_list = []
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', str(html))
    email_list.append(emails)
    return email_list

# This function removes duplicates from the list returned by getEmails()
# It will use a set to remove duplicates, then convert the set back to a list
def removeDuplicates(emails):
    email_list = []
    for email in emails:
        no_duplicates = list(set(email))
        for i in no_duplicates:
            email_list.append(i)
        return email_list

def printEmails(emails):
    for email in emails:
        print(email)

def main():
    url = getURL()
    html = getHTML(url)
    emails = getEmails(html)
    no_duplicates = removeDuplicates(emails)
    sorted_emails = sorted(no_duplicates)
    printEmails(sorted_emails)

main()