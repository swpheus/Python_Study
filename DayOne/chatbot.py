from socket import socket,AF_INET,SOCK_STREAM

s=socket(AF_INET,SOCK_STREAM)

s.bind(('0.0.0.0',5000))
s.listen(10)
print("Listening")

conn,addr=s.accept()

print(conn.recv(1024).decode())