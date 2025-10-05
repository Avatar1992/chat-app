# chat_client.py
import socket, threading, sys

HOST = '127.0.0.1'   # change to EC2 public IP later
PORT = 5000

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(4096).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Connection closed.")
            client.close()
            break

def write():
    while True:
        try:
            msg = input()
            if msg.lower() == "/quit":
                client.close()
                break
            full = f"{nickname}: {msg}"
            client.send(full.encode('utf-8'))
        except:
            break

if __name__ == "__main__":
    recv_thread = threading.Thread(target=receive, daemon=True)
    recv_thread.start()
    write()

