# This program will identify what kind of hash you are trying to crack, then use the appropriate hash cracking function to crack it.
# Author: imSiddis
# The following hash types are supported:
# MD5
# SHA1
# SHA224
# SHA256

import hashlib
import sys

class Hash:
    def __init__(self, hash):
        self.hash = hash
    def crack(self):
        hash = self.hash
        if len(hash) == 32:
            hash_type = "MD5"
        elif len(hash) == 40:
            hash_type = "SHA1"
        elif len(hash) == 56:
            hash_type = "SHA224"
        elif len(hash) == 64:
            hash_type = "SHA256"
        else:
            print("Hash type not supported.")
            sys.exit()
        print("Hash type: " + hash_type)
        print("Hash: " + hash)
        print("Cracking...")
        self.crack_hash(hash, hash_type)

    def crack_hash(self, hash, hash_type): # Hash cracking function
        if hash_type == "MD5":
            self.crack_md5(hash)
        elif hash_type == "SHA1":
            self.crack_sha1(hash)
        elif hash_type == "SHA224":
            self.crack_sha224(hash)
        elif hash_type == "SHA256":
            self.crack_sha256(hash)

    def crack_md5(self, hash): # MD5 hash cracking function
        wordlist = open("wordlist.txt", "r")
        for word in wordlist:
            word = word.strip()
            hash_object = hashlib.md5(word.encode())
            if hash_object.hexdigest() == hash:
                print("Password: " + word)
                sys.exit()
        print("Password not found in wordlist.")
        sys.exit()

    def crack_sha1(self, hash): # SHA1 hash cracking function
        wordlist = open("wordlist.txt", "r")
        for word in wordlist:
            word = word.strip()
            hash_object = hashlib.sha1(word.encode())
            if hash_object.hexdigest() == hash:
                print("Password: " + word)
                sys.exit()

    def crack_sha224(self, hash): # SHA224 hash cracking function
        wordlist = open("wordlist.txt", "r")
        for word in wordlist:
            word = word.strip()
            hash_object = hashlib.sha224(word.encode())
            if hash_object.hexdigest() == hash:
                print("Password: " + word)
                sys.exit()

    def crack_sha256(self, hash): # SHA256 hash cracking function
        wordlist = open("wordlist.txt", "r")
        for word in wordlist:
            word = word.strip()
            hash_object = hashlib.sha256(word.encode())
            if hash_object.hexdigest() == hash:
                print("Password: " + word)
                sys.exit()

def about(): # About function
    print("===================== HashCrack v1.0 ======================")
    print("                       By imSiddis")
    print("===========================================================")
    print("This program will crack a hash using a wordlist.")
    print("The following hash types are supported:")
    print("MD5")
    print("SHA1")
    print("SHA224")
    print("SHA256")
    print("This program is licensed under the GNU General Public License v3.0")
    # Press enter to return to the main menu
    input("Press enter to return to the main menu.")
    print("\n\n\n\n\n\n")

def generate_wordlist(): # This function should generate a wordlist.
    print("This function is not yet implemented.")

def crack_menu():
    print("===================== HashCrack v1.0 ======================")
    print("|                      By imSiddis                       |")
    print("==========================================================")
    print("| This program will crack a hash using a wordlist.       |")
    print("==========================================================")
    print("What would you like to do?")
    print("1. Crack a hash")
    print("2. Generate a wordlist (Coming soon!")
    print("3. About")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        hash = input("Enter the hash: ")
        hash = Hash(hash)
        hash.crack()
    elif choice == "2":
        generate_wordlist()
    elif choice == "3":
        about()
        crack_menu()
    elif choice == "0":
        sys.exit()

def main():
    crack_menu()

if __name__ == "__main__":
    main()