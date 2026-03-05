import socket
#A socket is like a virtual endpoint that allows two programs to communicate with each other — even if they’re on different computers.
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port (must match server) Both server and client are running on the same machine — your own laptop or PC.
HOST = '127.0.0.1'
PORT = 5000

# Connect to the server connect() initiates a TCP connection handshake with the server. This call blocks until connection succeeds (or fails with an exception).
client_socket.connect((HOST, PORT)) 
print("Connected to server. Type 'exit' to quit.")

while True:
    message = input("You: ")
    client_socket.send(message.encode())
    
    if message.lower() == 'exit':
        break
    
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

# Close connection
client_socket.close()
