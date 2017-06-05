import socket
import sys

try:
     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
     print("Failed to create socket")
     sys.exit()

try:
    mysock.bind(("",1234))
except socket.error:
     print("Failed to bind")
     sys.exit()
mysock.listen(5)
while True:
     conn, addr = mysock.accept()
     data = conn.recv(1000)
     print("Got it")
     if not data:
          break
     conn.sendall(data)

conn.close()
mysock.close()
