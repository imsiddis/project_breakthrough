import sid_mailscrape
import bs4
import requests
import threading

# This program will be a crawler. It will crawl a website and find all the links on the page.
# It will then crawl those links and find all the links on those pages.
# The amount of hops the crawler will take will be determined by the user during runtime.
# The crawler will also scrape emails from the pages it crawls and parse them through sid_mailscrape.py

# This function will be used to crawl a website and find all the links on the page.
# It will then return a list of all the links on the page.

def crawl(url):
    # First, we will get the HTML of the page.
    page = requests.get(url)
    # Then we will parse the HTML using beautifulsoup.
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    # Now we will find all the links on the page.
    links = soup.find_all("a")
    # We will now create a list to store the links in.
    link_list = []
    # We will now loop through the links and add them to the list.
    for link in links:
        link_list.append(link.get("href"))
    # We will now return the list of links.
    return link_list

class Spider:
    def __init__(self, url, hops):
        self.url = url
        self.hops = hops
        self.links = []
        self.emails = []
        self.emails.append(sid_mailscrape.get_emails(self.url))
        self.links.append(crawl(self.url))
        self.hop_count = 0
        self.hop()

    def hop(self):
        if self.hop_count < self.hops:
            for link in self.links:
                self.emails.append(sid_mailscrape.get_emails(link))
                self.links.append(crawl(link))
            self.hop_count += 1
            self.hop()
        else:
            return self.emails
    # Will add https:// to the start of the URL if it is not there.
    def add_https(self):
        if self.url.startswith("https://"):
            return self.url
        else:
            self.url = "https://" + self.url
            return self.url

def main():
    url = input("Enter the URL to crawl: ")
    hops = int(input("Enter the number of hops: "))
    spider = Spider(url, hops)
    print(spider.emails)

main()