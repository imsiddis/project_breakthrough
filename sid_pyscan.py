# This program will request an IP with a CIDR notation from the user in the CLI.
# The program will then scan the IP for active hosts on the network.
# The program will attempt to resolve hostnames of the hosts found during the scan.

# The user will be prompted to enter an IP address.
# If the IP address is invalid, the user will be prompted to enter a valid IP address.
# If the IP address includes a CIDR notation, it will be used to scan the network instead of the IP address.
# If the IP address does not include a CIDR notation, the specified IP address will be scanned.
import sid_main
import scapy.all as scapy
import socket

#========================#
# Build Version Variable #
#========================#
build_num = 0.1

# This function will request an IP address from the user.
def get_ip():
    while True:
        try:
            print("Type 'q' to quit.")
            ip = input("Enter an IP address: ")
            if "/" in ip:
                return ip
            elif ip == "q":
                break
            else:
                socket.inet_aton(ip)
                return ip
        except:
            print("Invalid IP address. Please try again.")


# This function will use scapy to scan the network for active hosts.
# It will return a list of dictionaries containing the IP address and MAC address of each host.
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\t\t\tHostname")
    print("--------------------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"] + "\t\t" + get_hostname(client["ip"]))
        # print(client["ip"] + "\t\t" + client["mac"])

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        return hostname[0]
    except:
        return "No hostname found."

def start():
    try:
        sid_main.clear_screen()
        print("#=====================#")
        print(f"|     NetScan v{build_num}    |")
        print("|   By imSiddis       |")
        print("#=====================#================================================================#")
        print("| Info:                                                                                |")
        print("| This program will scan the network for active hosts.                                 |")
        print("| The program will attempt to resolve hostnames of the hosts found during the scan.    |")
        print("| You can enter an IP address with a CIDR notation to scan a network.                  |")
        print("| If you do not enter a CIDR notation, the program will scan the specified IP address. |")
        print("#====================#=================================================================#")
        print("| 1. Scan Network/IP |")
        print("| 0. Back            |")
        print("#====================#")
        user_choice = input("Enter choice: ")

        if user_choice == "1":
            start_scan()
        elif user_choice == "0":
            sid_main.main()
        else:
            print("Invalid choice")
            input("Press Enter to try again.")
            start()
    except KeyboardInterrupt as e:
        print("Program killed.")

def start_scan():
    ip = get_ip()
    scan_result = scan(ip)
    print_result(scan_result)
    input("Press Enter to return to menu.")
    start()
