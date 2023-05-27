'''
After reviewing and studying Chapter 2 in Black Hat Python you are to create a Standalone Python script that will act as a TCP client. 
The client will connect to the TCP server created in Assignment 10 on Port 5555.  The client will send 10 messages (in an automated fashion)
to the server with differing content, receive the MD5 hash response provided by the TCP server, and print the original message and MD5 hash. 

You will submit:

1) Your final python script

2) A screenshot of all the messages and the received hashed messages
'''
'''
Sarah Shinn
3/1/2023
Assignment 11
'''


import socket
import hashlib

target_host = "localhost"
target_port = 5555

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

# Send 10 messages to the server
for i in range(10):
    message = f"Message {i}"
    #send some data
    client.send(message.encode('utf-8'))

    #receive the MD5 hash from the server
    response = client.recv(1024).decode('utf-8')

    #print the original message and the MD5 hash
    print(f"Original message: {message}")
    print(f"MD5 hash: {response}")

#close the client socket
client.close()