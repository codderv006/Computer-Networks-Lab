TCP
Client.py
import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send data to the server
message = "Hello,"
client_socket.send(message.encode('utf-8'))

# Receive and print the response
response = client_socket.recv(1024).decode('utf-8')
print("Received response from server: {}".format(response))

# Close the socket
client_socket.close()

Server.py
import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (maximum 1 connection in the queue)
server_socket.listen(1)

print("TCP server is listening on {}:{}".format(*server_address))

while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()

    print("Accepted connection from {}:{}".format(*client_address))

    data = client_socket.recv(1024).decode('utf-8')
    print("Received data: {}".format(data))

    response = "Hello, client!"
    client_socket.send(response.encode('utf-8'))

    client_socket.close()









UDP

Server.py
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 5678)
server_socket.bind(server_address)

print("UDP server is listening on {}:{}".format(*server_address))

while True:
    print("Waiting for a message...")
    data, client_address = server_socket.recvfrom(1024)
    print("Received data from {}:{}".format(*client_address))
    print("Data: {}".format(data.decode('utf-8')))

    response = "Hello, UDPclient!"
    server_socket.sendto(response.encode('utf-8'), client_address)

Client.py
import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 5678)

# Send data to the server
message = "Hello, server!"
client_socket.sendto(message.encode('utf-8'), server_address)

# Receive and print the response
response, server_address = client_socket.recvfrom(1024)
print("Received response from server: {}".format(response.decode('utf-8')))


# Close the socket
client_socket.close()
