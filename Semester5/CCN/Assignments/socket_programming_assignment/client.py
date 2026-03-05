import socket
import threading
import pyaudio

# Audio Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Server details (same PC)
SERVER_IP = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
print("[CLIENT] Connected to server")

# Initialize Audio
p = pyaudio.PyAudio()
stream_in = p.open(format=FORMAT, channels=CHANNELS,
                   rate=RATE, input=True, frames_per_buffer=CHUNK)
stream_out = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, output=True, frames_per_buffer=CHUNK)

def send_audio():
    while True:
        data = stream_in.read(CHUNK, exception_on_overflow=False)
        client_socket.sendall(data)

def receive_audio():
    while True:
        data = client_socket.recv(CHUNK)
        if not data:
            break
        stream_out.write(data)

# Run both threads
threading.Thread(target=send_audio).start()
threading.Thread(target=receive_audio).start()
