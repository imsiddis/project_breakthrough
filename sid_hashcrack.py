# This program will identify what kind of hash you are trying to crack, then use the appropriate hash cracking function to crack it.
# Author: imSiddis
# The following hash types are supported:
# MD5
# SHA1
# SHA224
# SHA256

import hashlib
import sys
import threading
import time
import os
import re
import urllib.request

# This function will take a hash as input, then use the hashlib library to crack it
def crackHash(hash):
    # The following code will crack an MD5 hash
    if len(hash) == 32:
        print("Cracking an MD5 hash...")
        wordlist = input("Enter a wordlist to use: ")
        try:
            with open(wordlist, "r") as wordlist:
                for word in wordlist:
                    word = word.strip()
                    hash_object = hashlib.md5(word.encode())
                    hex_dig = hash_object.hexdigest()
                    if hex_dig == hash:
                        print("The hash has been cracked! The password is: " + word)
                        break
                    else:
                        print("The password is not: " + word)
        except FileNotFoundError:
            print("The wordlist you entered does not exist")
    # The following code will crack a SHA1 hash
    elif len(hash) == 40:
        print("Cracking a SHA1 hash...")
        wordlist = input("Enter a wordlist to use: ")
        try:
            with open(wordlist, "r") as wordlist:
                for word in wordlist:
                    word = word.strip()
                    hash_object = hashlib.sha1(word.encode())
                    hex_dig = hash_object.hexdigest()
                    if hex_dig == hash:
                        print("The hash has been cracked! The password is: " + word)
                        break
                    else:
                        print("The password is not: " + word)
        except FileNotFoundError:
            print("The wordlist you entered does not exist")
    # The following code will crack a SHA224 hash
    elif len(hash) == 56:
        print("Cracking a SHA224 hash...")
        wordlist = input("Enter a wordlist to use: ")
        try:
            with open(wordlist, "r") as wordlist:
                for word in wordlist:
                    word = word.strip()
                    hash_object = hashlib.sha224(word.encode())
                    hex_dig = hash_object.hexdigest()
                    if hex_dig == hash:
                        print("The hash has been cracked! The password is: " + word)
                        break
                    else:
                        print("The password is not: " + word)
        except FileNotFoundError:
            print("The wordlist you entered does not exist")
    # The following code will crack a SHA256 hash
    elif len(hash) == 64:
        print("Cracking a SHA256 hash...")
        wordlist = input("Enter a word)list to use: ")