# Program to simulate following truck
# by Maxwell Ern, 4/2/21
# The following program will receive two client packets and send 
# two ack packets. When the client disconnects, the program will
# signal that it is closing the socket and then quit execution.

import socket
import time

#initial server values, mostly taken from provided project files
addr = "192.168.1.173"
port = 6789
pos = "14 S 368058 3899192"
vel = 110.0
t_sec = 0.2

#print initial values
print("Initial GPS Position: %s" %(pos))
print("Initial Velocity: %.1fkm/h" %(vel))
print("Time Interval: %.1fs" %(t_sec))
print("============================================")

#create socket
servSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connect to client
servSock.bind((addr, port))

#takes variable list and conjoins into a string
def getVarString(x):
    s1 = ""
    return(s1.join(x))

#prints a socket closing notification before ending program
def socketClosed(num):
    print("Type = Socket Disconnection")
    print("Sequence No. = %s\n" %(num))
    quit()

#extracts variables from packet and prints results as they are interpreted
def printPacketStats(packet):

    print("Packet Received:")
    arr = list(packet) #splits up packet variables into list
    i = 0 #counter to go through arr list

    # I originally wanted the following lines to be contained
    # in one big while loop, but I kept getting IndexOutOfBounds 
    # and ran out of time to solve the issue :(

    #first is sequence number
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    seq_num = getVarString(temp)
    i = i + 1

    if(seq_num == "99999"): # my program uses sequence number to signal when
        servSock.close()    # to close the socket
        socketClosed(seq_num)
    
    print("Sequence No. = %s" %(seq_num))

    #second is client ip address
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_ip = getVarString(temp)
    i = i + 1
    print("IP = %s" %(client_ip))

    #third is client position
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_pos = getVarString(temp)
    i = i + 1
    print("GPS Position = %s" %(client_pos))
    
    #fourth is client velocity
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_velocity = getVarString(temp)
    i = i + 1
    print("Velocity = %s" %(client_velocity))

    #fifth is client acceleration
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_accel = getVarString(temp)
    i = i + 1
    print("Acceleration = %s" %(client_accel))

    #sixth is client brake control
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_bc = getVarString(temp)
    i = i + 1
    print("Brake Control = %s" %(client_bc))

    #last one is client gas throttle
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_gt = getVarString(temp)
    i = i + 1
    print("Gas Throttle = %s\n" %(client_gt))

    return seq_num #returns packet's sequence number to use in the ack packet

#prints the ack packet when successfully sent
def printPacketSent(num):
    print("Ack Packet Sent:")
    print("Type = Ack")
    print("Sequence No. = %s\n" %(num))



#main while loop to operate under
while True:
    #receive packet from lead truck
    data, addr = servSock.recvfrom(1024)
    client_pack = bytes.decode(data)

    #print received packet
    ack_num = printPacketStats(client_pack)
    
    #create and send ack
    data = str(ack_num)
    ack = str.encode(data)
    servSock.sendto(ack, addr)
    printPacketSent(ack_num) #print the sent ack packet

    time.sleep(t_sec) #wait a bit before receiving more packets




