import socket
#import struct

#initial values
seq_num = 5895
addr = "192.168.1.173"
port_num = 6789
pos = "14 S 368052 3899189"
vel = 110.99
accel = 1.38
brk_ctrl = 0.0
throttle = 0.46

#prepare packet data
s = str(seq_num) + "," + str(addr) + "," + str(pos) + "," + str(vel)
s += "," + str(accel) + "," + str(brk_ctrl) + "," + str(throttle)

#print(s)
data = str.encode(s)

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send packet
clientSock.sendto(data, (addr, port_num))
print("Packet Sent:")