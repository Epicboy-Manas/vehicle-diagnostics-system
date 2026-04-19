import socket
import random
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def detect_faults(temp, voltage, speed):
    faults = []

    if temp > 80:
        faults.append("Overheating")
    if voltage > 250:
        faults.append("Overvoltage")
    if speed > 100:
        faults.append("Overspeed")

    return faults

def log_data(data):
    with open("log.txt", "a") as f:
        f.write(data + "\n")

print("🚗 Vehicle Diagnostics System Started...\n")

while True:
    temp = random.randint(20, 100)
    voltage = random.randint(200, 260)
    speed = random.randint(0, 120)

    faults = detect_faults(temp, voltage, speed)

    message = f"{datetime.now()} | Temp:{temp}, Volt:{voltage}, Speed:{speed}, Faults:{faults}"

    print("📤 Sending:", message)

    log_data(message)

    client.send(message.encode())

    time.sleep(1)
