# This program will be the main function in this project and will include a menu to allow the user to choose what they want to do.
#=============================#
# Import the required modules #
#=============================#
import sid_hashcrack
import sid_mailscrape
import sid_pyscan
import os
# import sid_dos
# import sid_networkscanner

#========================#
# Build Version variable #
#========================#
build_ver = 0.1

#=============================#
# Define the main function    #
#=============================#
def main():
    clear_screen()
    print("=========================================")
    print(f"|     imSiddis PenTest Toolbox v{build_ver}     |")
    print("=========================================")
    print("1. HashCrack")
    print("2. MailScrape")
    print("3. DoS")
    print("4. Network Scanner")
    print("5. About")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        sid_hashcrack.start()
    elif choice == "2":
        sid_mailscrape.start(emails=None)
    elif choice == "3":
        pass
        # sid_dos.main()
    elif choice == "4":
        sid_pyscan.start()

    elif choice == "5":
        about()
        input("Press enter to return to the menu")

    elif choice == "0":
        confirm_exit()
    else:
        print("Invalid choice")
        main()

#=============================#
# Define the about function   #
#=============================#
def about():
    clear_screen()
    print(f"======================= MailScrape v{build_ver} ========================")
    print("This program is designed to be an exercise in Python programming.\nIt is a collection of programs that I have written to help me learn Python.\nThe chosen theme for this project are pentesting tools.")
    print("=================================================================")
    input("Press enter to return to the menu")
    main()

#==============#
# Confirm Exit #
#==============#
def confirm_exit():
    print("Are you sure you want to exit? (Y/n)") # Ask the user if they want to exit
    choice = input("Enter your choice: ")
    if choice == "Y" or choice == "y" or choice == "":
        print("Exiting...")
        exit()
    elif choice == "N" or choice == "n":
        main()
    else:
        print("Invalid choice")
        confirm_exit()

#==============#
# Clear Screen #
#==============#
def clear_screen():
    try:
        os.system("cls")
    except:
        os.system("clear")

if __name__ == '__main__':
    main()