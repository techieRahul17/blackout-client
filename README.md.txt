# Blackout Client

This package runs a blackout screen overlay on client systems, controlled via a Socket.IO server.

## Features
- Full-screen blackout overlay
- Motivational quotes
- Socket.IO server controlled blackout/start/stop
- Cross-platform (Windows & Linux)

---

## Installation

### 1. Ensure pip is installed
Linux / Mac:
```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

Windows:
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip

### 2. Install from GitHub
```bash
pip install git+https://github.com/your-username/blackout-client.git

####Usage

Run the client:

blackout-client


By default, it connects to:
```bash
http://10.6.3.36:3000


###You can edit client.py to set your own server IP.

##Dependencies
```bash
Python 3.7+
```bash
Tkinter (usually bundled with Python)
```bash
On Linux: sudo apt install python3-tk
```bash
python-socketio (installed automatically)