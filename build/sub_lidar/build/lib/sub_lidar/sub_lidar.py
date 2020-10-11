import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socket
import math
import time
import os
import struct



#-----------------------TCP/IP---------------------------
def connection(socket):
    while True:
        conn, address = socket.accept()
        if address:
            print("conn: {} \naddress: {}".format(conn, address))
            break
        print("connecting...\n")
        time.sleep(2)

def createSocket():
    # Server
    # Create new server socket

    HOST = '192.168.0.105' #socket.gethostname()
    PORT = 64405
    os.system("fuser -k {}/tcp".format(PORT))
    time.sleep(0.5)
    # socket.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)

    try:
        print("connecting... {}:{}\n".format(HOST, PORT))
        conn, address = sock.accept()
        print("conn: {} \naddress: {}\n".format(conn, address))
    except:
        print("Fail connected !")
    return conn, address

    
#-----------------------TCP/IP---------------------------


def main():
    #-----------------------TCP/IP---------------------------
    conn, address = createSocket()
    # connection(sock)
    #-----------------------TCP/IP---------------------------
    
    print('Hi from sub_lidar.')
    while True:
        data=conn.recv(1500)
        if not data: continue
        out = []
        for x in  range(int(len(data)/4)):
            xx = struct.unpack('<f', data[x*4:x*4+4])
            out.append(round(xx[0], 3))
        print(out)
        # print(struct.unpack('<f', data))   #little endian

if __name__ == '__main__':
    main()
