#
# import socket
#
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# serve_address = ('localhost', 12434)
# server_socket.bind(serve_address)
# server_socket.listen(5)
# print("Server is listening...")
#
# while True:
#     print("waiting for connection...")
#     client_socket, client_address = server_socket.accept()
#     print("Accepted connection.")
#     try:
#         data = client_socket.recv(1024).decode('utf-8')
#         print("Received data: {}".format(data))
#
#         response = "Hello client!"
#         client_socket.send(response.encode('utf-8'))
#     finally:
#         client_socket.close()


import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('localhost', 13245)
server_socket.bind(server_addr)

server_socket.listen(5)
print("server is listening....")

while True:
    print("Waiting for connection...")
    client_socket, client_addr = server_socket.accept()
    print("Connection established.")
    try:
        data = client_socket.recv(1024).decode('utf-8')
        print("data received is: {}".format(data))

        response = "Hello client!"
        server_socket.send(response.encode('utf-8'))
    finally:
        server_socket.close()