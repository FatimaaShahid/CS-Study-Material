import socket, threading, pyaudio

# Audio setup
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Network setup
IP = "10.200.254.229"  # listen on all network interfaces
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)
print("[SERVER] Waiting for connection...")

conn, addr = server_socket.accept()
print(f"[CONNECTED] Client connected from {addr}")

audio = pyaudio.PyAudio()
stream_in = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                       input=True, frames_per_buffer=CHUNK)
stream_out = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        output=True, frames_per_buffer=CHUNK)

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

threading.Thread(target=send_audio, daemon=True).start()
threading.Thread(target=receive_audio, daemon=True).start()

print("[SERVER] Voice call active. Talk now!")
threading.Event().wait()  # keep main thread alive
