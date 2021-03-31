import socket
import struct

counter = 1000 #for sequence number

def string_conversion(velocity, time, pos, client_addr, seq_num):
    response = "*****Leading Truck Stats*****"
    response += "\nSequence #: %d" %(seq_num)
    response += "\nVelocity: %.1f" %(velocity)
    response += "\nTime: %.1f" %(time)
    response += "\nPosition: %s" %(pos)
    response += "\nAddress: %s" %(client_addr)
    return str.encode(response)

bytesToSend = string_conversion(110.0, 0.2, "14 S 368056 3899192", "192.168.1.173", counter)

serverAddressPort = ("192.168.1.173", 20001)
bufferSize = 1024

#Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0])

print(msg)