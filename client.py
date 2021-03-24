import socket

#initial values
velocity = 110.0
time = 0.2
position = '14 S 368056 3899192'
client_addr = "192.168.1.173"
seq_num = 1

msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
print("Encoded string: %s" %(bytesToSend))

serverAddressPort = ("192.168.1.173", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0])

print(msg)