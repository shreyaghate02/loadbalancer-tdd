import socket
​
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',15004))
server.listen(1)
server.setblocking(0)
connection =[]
while True:
    try:
        conn, add = server.accept()
        connection.append(conn)
        conn.setblocking(0)
    except Exception as e:
        pass
    
    for c in connection:
        try:
            data = c.recv(1000)
            print(data)
            print(len(data))
            c.sendall("HTTP/1.1 200 OK\r\nContent-Length: %s\r\n\r\n%s" % (len(data),data))      
        except Exception as e:
            pass