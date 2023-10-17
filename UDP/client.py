# import socket
#
# # Create a UDP socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Server address
# server_address = ('localhost', 56718)
#
# # Send data to the server
# message = "Hello, server!"
# client_socket.sendto(message.encode('utf-8'), server_address)
#
# # Receive and print the response
# response, server_address = client_socket.recvfrom(1024)
# print("Received response from server: {}".format(response.decode('utf-8')))
#
#
# # Close the socket
# client_socket.close()

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12355)

message = "Hello world!"
client_socket.sendto(message.encode('utf-8'), server_address)

response, server_address = client_socket.recvfrom(1024)
print("response received is {}".format(response.decode('utf-8')))

client_socket.close()