# import socket
#
# # Create a UDP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Bind the socket to a specific address and port
# server_address = ('localhost', 56718)
# server_socket.bind(server_address)
#
# print("UDP server is listening on {}:{}".format(*server_address))
#
# while True:
#     print("Waiting for a message...")
#     data, client_address = server_socket.recvfrom(1024)
#     print("Received data from {}:{}".format(*client_address))
#     print("Data: {}".format(data.decode('utf-8')))
#
#     response = "Hello, UDPclient!"
#     server_socket.sendto(response.encode('utf-8'), client_address)

import socket

serve_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12355)
serve_socket.bind(server_addr)

while True:
    print("waiting for connection...")
    data, client_addr = serve_socket.recvfrom(1024)
    print("data received: {}".format(data.decode('utf-8')))

    response = "hello client!"
    serve_socket.sendto(response.encode('utf-8'), client_addr)

serve_socket.close()