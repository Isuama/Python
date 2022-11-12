import socket

# create socket object
print('Creating socket...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
print('connection with remote host')
target_host = "localhost"
target_port = 8080
s.connect((target_host, target_port))
print('connection ok')

# connect the client to the remote host and send some data
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" %target_host
s.send(request.encode())

# receive some data back and print out the response
data = s.recv(4096)
print("Data", str(bytes(data)))
print("Length", len(data))
print('closing the socket')
s.close()
