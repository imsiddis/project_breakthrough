# This program will be the main function in this project and will include a menu to allow the user to choose what they want to do.
#=============================#
# Import the required modules #
#=============================#
# import sid_hashcrack.py
# import sid_mailscrape.py
# import sid_dos.py
# import sid_networkscanner.py

#=============================#
# Define the main function    #
#=============================#
def main():
    print("=========================================")
    print("|     imSiddis PenTest Toolbox v1.0     |")
    print("=========================================")
    print("1. HashCrack")
    print("2. MailScrape")
    print("3. DoS")
    print("4. Network Scanner")
    print("5. About")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
        # hashcrack.main()
    elif choice == "2":
        pass
        # mailscrape.main()
    elif choice == "3":
        pass
        # dos.main()
    elif choice == "4":
        pass
        # networkscanner.main()
    elif choice == "5":
        pass
        # about()
        # input("Press enter to return to the menu")

    elif choice == "0":
        # confirm_exit()
        pass
    else:
        print("Invalid choice")
        main()

#=============================#
# Define the about function   #
#=============================#
def about():
    pass