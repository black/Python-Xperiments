import socket, threading

def ReceivePackets():
    soc = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))  
    while 1:
        packet = soc.recv(2000)  
        buffer.append(packet)

def ReadSniffer():
    result = list(buffer) 
    #Clear buffer to start sniffing from scratch after reading
    del buffer[:]
    return result