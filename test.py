import socket
from contextlib import closing
   
def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
        else:
            print("Port is not open")





host="192.168.200.50"
port=22
check_socket(host, port)
