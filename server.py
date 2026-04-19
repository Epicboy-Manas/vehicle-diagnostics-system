import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("🖥️ Server started. Waiting for connection...")

conn, addr = server.accept()
print(f"✅ Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    message = data.decode()
    print("\n📥 Received:", message)

    # 🚨 Alert system
    if "Overheating" in message:
        print("🚨 CRITICAL ALERT: Overheating detected!")
    if "Overvoltage" in message:
        print("🚨 CRITICAL ALERT: Overvoltage detected!")
    if "Overspeed" in message:
        print("🚨 CRITICAL ALERT: Overspeed detected!")

conn.close()
