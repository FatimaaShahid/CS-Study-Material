import socket
import threading
import pyaudio

# Audio Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Server Setup
IP = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)
print("[SERVER] Waiting for connection...")

conn, addr = server_socket.accept()
print(f"[CONNECTED] Client connected from {addr}")

# Initialize Audio
p = pyaudio.PyAudio()
stream_in = p.open(format=FORMAT, channels=CHANNELS,
                   rate=RATE, input=True, frames_per_buffer=CHUNK)
stream_out = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, output=True, frames_per_buffer=CHUNK)

def send_audio():
    while True:
        data = stream_in.read(CHUNK, exception_on_overflow=False)
        conn.sendall(data)

def receive_audio():
    while True:
        data = conn.recv(CHUNK)
        if not data:
            break
        stream_out.write(data)

# Run both threads
threading.Thread(target=send_audio).start()
threading.Thread(target=receive_audio).start()
