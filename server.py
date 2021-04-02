import socket
import time

#initial server values
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

def socketClosed(num):
    print("Type = Socket Disconnection")
    print("Sequence No. = %s\n" %(num))
    quit()

#extract values from packet and print results
def printPacketStats(s):
    print("Packet Received:")
    i = 0
    arr = list(s)

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
        servSock.close()    # the client wishes to disconnect
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

    #lastly is client gas throttle
    temp = []
    while (arr[i] != ','):
        temp.append(arr[i])
        i = i + 1
    client_gt = getVarString(temp)
    i = i + 1
    print("Gas Throttle = %s\n" %(client_gt))

    return seq_num #this is for ack
    
def printPacketSent(num):
    print("Ack Packet Sent:")
    print("Type = Ack")
    print("Sequence No. = %s\n" %(num))

def createAck(n):
    ack = str(n)
    return str.encode(ack) #convert list of variables to bytes

#while loop to operate under
while True:
    #receive packet from client
    data, addr = servSock.recvfrom(1024)
    client_pack = bytes.decode(data)

    #print received packet
    ack_num = printPacketStats(client_pack)
    
    #create and send ack
    data = str(ack_num)
    ack = str.encode(data)
    
    #servSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servSock.sendto(ack, addr)
    printPacketSent(ack_num) #print the sent ack

    time.sleep(t_sec) #wait a bit before receiving more packets




