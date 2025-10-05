# chat_server.py
import socket, threading

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []
lock = threading.Lock()

def broadcast(message, _except=None):
    with lock:
        for client in clients:
            if client is _except:
                continue
            try:
                client.send(message)
            except:
                # ignore broken sockets here; handler will cleanup
                pass

def handle(client):
    while True:
        try:
            message = client.recv(4096)
            if not message:
                break
            broadcast(message, _except=None)
        except:
            break

    # cleanup
    with lock:
        if client in clients:
            idx = clients.index(client)
            clients.remove(client)
            try:
                nickname = nicknames.pop(idx)
                broadcast(f"{nickname} left the chat!".encode('utf-8'))
            except:
                pass
            client.close()

def accept_clients():
    print(f"Server listening on {HOST}:{PORT} ...")
    while True:
        client, addr = server.accept()
        print("Connected by", addr)
        # ask for nickname
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        with lock:
            nicknames.append(nickname)
            clients.append(client)
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,), daemon=True)
        thread.start()

if __name__ == "__main__":
    accept_clients()

