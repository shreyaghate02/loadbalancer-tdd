import socket
import time

HOST = '127.0.0.1'                 
PORT = 15000             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
s.setblocking(0)

conn, addr = s.accept()
print 'Connected by', addr
while 1:
  data = conn.recv(1024)
  if not data: break
  conn.sendall(data)
conn.close()