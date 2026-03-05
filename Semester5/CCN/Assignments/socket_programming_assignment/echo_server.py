import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET — it tells python that ipv4 will be used

# socket.SOCK_STREAM — SOCK_STREAM tells Python that you want to use the TCP protocol — a reliable, connection-oriented data stream.

# Define host and port
HOST = '127.0.0.1'  # localhost only accept connections from the same machine
PORT = 5000

# Bind the socket to address and port
server_socket.bind((HOST, PORT))

# Start listening for connections
server_socket.listen(1)
print(f"Server started on {HOST}:{PORT}... Waiting for connection.")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# accept() blocks until a client connects. It returns:
# conn: a new socket object for communication with that client (separate from server_socket)
# addr: the client’s address tuple (ip, port)

# Echo messages back to the client
while True:
    data = conn.recv(1024).decode() #conn.recv(1024) reads up to 1024 bytes from client — this call blocks until data arrives.
    if not data or data.lower() == 'exit': #if not data (closed)
        print("Connection closed.")
        break
    print(f"Client: {data}")
    conn.send(data.encode())  # send same message back

# Close the connection
conn.close()
server_socket.close()

#the server does send messages to the client —
# but only as a response (an echo) to what the client sends.
