import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print(error)

port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror as error:
    print(error)
    sys.exit()

s.connect((host_ip,port))

print("end")