'''
After Reviewing and Studying Chapter 2 in Black Hat Python you are to create a standalone Python script that will act as a TCP server.
The server will accept connections on port 5555 from TCP clients operating on the same local IP range as the server.
The server will receive the message, create a MD5 hash of the message, print the message and MD5 hash of the message, and respond to the TCP client 
with the MD5 hash generated. 
The server will continue to operate until terminated by the user.

You will submit:

1) Your final python script

2) A screenshot of all the connections, messages, and hashed messages
'''
'''
Sarah Shinn
3/1/2023
Assignment 10
'''



import socket
import threading
import hashlib

bind_ip = "0.0.0.0"
bind_port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            break
        print("[*] Received: %s" % request)
        
        md5_hash = hashlib.md5(request.encode('utf-8')).hexdigest()
        
        client_socket.send(md5_hash.encode('utf-8'))

        print("[*] Sent MD5 hash: %s" % md5_hash)

    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Accepted connection from %s:%d" % (addr[0],addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
