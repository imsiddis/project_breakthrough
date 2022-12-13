# This program will be the main function in this project and will include a menu to allow the user to choose what they want to do.
#=============================#
# Import the required modules #
#=============================#
# import sid_hashcrack
import sid_mailscrape
# import sid_dos
# import sid_networkscanner

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
        # sid_hashcrack.main()
    elif choice == "2":
        sid_mailscrape.start(emails=None)
    elif choice == "3":
        pass
        # sid_dos.main()
    elif choice == "4":
        pass
        # sid_networkscanner.main()

    elif choice == "5":
        about()
        input("Press enter to return to the menu")

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
    print("======================= MailScrape v1.0 ========================")
    print("This program is designed to be an exercise in Python programming.\nIt is a collection of programs that I have written to help me learn Python.\nThe chosen theme for this project are pentesting tools.")
    print("=================================================================")
    input("press enter to return to the menu")
    main()

if __name__ == '__main__':
    main()