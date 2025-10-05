# Test locally 

python3 chat_server.py
python3 chat_client.py
choose different nicknames and chat

# Prerequisites

AWS account with permissions to create EC2 instances and security groups.

Local machine with python3 and git.

An SSH key pair for EC2 (or create one in AWS Console).

Basic terminal / SSH familiarity

# Project overview (what & why)

Server: TCP server that accepts many clients, broadcasts messages to all connected clients.

Client: Connects to server, sends/receives messages.

Why: Learn sockets, threading, simple network architecture, deploying to cloud (EC2).
