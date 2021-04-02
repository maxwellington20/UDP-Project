import socket
import time

#initial values
seq_num = 5895
addr = "192.168.1.173"
port_num = 6789
pos = "14 S 368052 3899189"
vel = 110.0
t_sec = 0.2
accel = 1.38
brk_ctrl = 0.0
throttle = 0.46

#print initial values
print("Initial GPS Position: %s" %(pos))
print("Initial Velocity: %.1fkm/h" %(vel))
print("Time Interval: %.1fs" %(t_sec))
print("============================================")

#prepare client_pack data
def createPacket():
    client_pack = str(seq_num) + "," + str(addr) + "," + str(pos) + "," + str(vel)
    client_pack += "," + str(accel) + "," + str(brk_ctrl) + "," + str(throttle) + ","
    return str.encode(client_pack) #convert list of variables to bytes

#print packet info
def printPacketSent():
    print("Packet Sent:")
    print("Sequence No. = %d" %(seq_num))
    print("IP = %s" %(addr))
    print("GPS Position = %s" %(pos))
    print("Velocity = %.2f" %(vel))
    print("Acceleration = %.2f" %(accel))
    print("Brake Control = %.1f" %(brk_ctrl))
    print("Gas Throttle = %.2f\n" %(throttle))

#print ack info
def printPacketRecv(num):
    print("Packet Received:")
    print("Type = Ack")
    print("Sequence No. = %s\n" %(num))

#connect to server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendAndReceive(serv_addr): #made this to streamline the testing proccess
    #send client packet
    data = createPacket()
    clientSock.sendto(data, (serv_addr, port_num))
    printPacketSent()

    while True:
        time.sleep(t_sec) #wait a bit before looking to recieve
        data, serv_addr = clientSock.recvfrom(1024) #recieve server packet
        serv_pack = bytes.decode(data)
        printPacketRecv(serv_pack)
        break

sendAndReceive(addr) #execute with original info


# in order to follow the scripts provided in the project1 folder on canvas,
# I manually code changes in data here rather than in the terminal

#change one
seq_num += 1
pos = "14 S 368048 3899185"
vel = 112.88
accel = 2.63
throttle = 0.46
sendAndReceive(addr) #execute with new changes

