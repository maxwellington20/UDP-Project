import socket
#import struct

serv_addr = "192.168.1.173"
serv_port = 6789

servSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servSock.bind((serv_addr, serv_port))

while True:
    print("Server Listening...")

    data, addr = servSock.recvfrom(1024)

    s = bytes.decode(data)

    print(s)
