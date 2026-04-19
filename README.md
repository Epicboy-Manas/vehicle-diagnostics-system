# Embedded Linux-Based Vehicle Diagnostics System

## Overview
A real-time vehicle diagnostics system that simulates sensor data, detects faults, logs system activity, and transmits data to a control server.

## Features
- Real-time data simulation (temperature, voltage, speed)
- Fault detection (overheating, overvoltage, overspeed)
- Data logging with timestamps
- Client-server communication using sockets
- Real-time alert system on server

## Technologies Used
- Python
- Linux (Ubuntu)
- Socket Programming

## How to Run

### Step 1: Start Server
python3 server.py

### Step 2: Start Client
python3 client.py
