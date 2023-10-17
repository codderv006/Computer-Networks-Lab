# import socket
#
# # Create a TCP socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect to the server
# server_address = ('localhost', 12434)
# client_socket.connect(server_address)
#
# try:
#     # Send data to the server
#     message = "Hello,"
#     client_socket.send(message.encode('utf-8'))
#
#     # Receive and print the response
#     response = client_socket.recv(1024).decode('utf-8')
#     print("Received response from server: {}".format(response))
# finally:
#     # Close the socket
#     client_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('localhost', 13245)

client_socket.connect(server_addr)

try:
    message = "Hello world"
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print("received responose {}".format(response))
finally:
    client_socket.close()