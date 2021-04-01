import socket
#import struct

#initial values
seq_num = 5895
addr = "192.168.1.173"
port_num = 6789
pos = "14 S 368052 3899189"
vel = 110.0
time = 0.2
accel = 1.38
brk_ctrl = 0.0
throttle = 0.46

#print initial values
print("Initial GPS Position: %s" %(pos))
print("Initial Velocity: %.1fkm/h" %(vel))
print("Time Interval: %.1fs" %(time))
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
    print("Gas Throttle = %.2f" %(throttle))

#connect to server
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send client_pack
data = createPacket()
clientSock.sendto(data, (addr, port_num))
printPacketSent()