# import socket
# import threading

# # --- Server Configuration ---
# HOST = '127.0.0.1'   # localhost
# PORT = 5555          # free port number

# # --- Server socket setup ---
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen()

# print(f" Server started on {HOST}:{PORT} and waiting for clients...")

# clients = []   # all connected clients
# nicknames = [] # nicknames of clients


# # --- Broadcast message to all clients ---
# def broadcast(message):
#     for client in clients:
#         try:
#             client.send(message)
#         except:
#             pass


# # --- Handle messages from a single client ---
# def handle_client(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             if not message:
#                 break
#             broadcast(message)
#         except:
#             # client disconnected
#             if client in clients:
#                 index = clients.index(client)
#                 nickname = nicknames[index]
#                 clients.remove(client)
#                 nicknames.remove(nickname)
#                 client.close()
#                 broadcast(f" {nickname} left the chat.".encode('utf-8'))
#             break


# # --- Accept new client connections ---
# def receive_connections():
#     while True:
#         client, address = server.accept()
#         print(f" Connected with {address}")

#         client.send("NICK".encode('utf-8'))
#         nickname = client.recv(1024).decode('utf-8')

#         nicknames.append(nickname)
#         clients.append(client)

#         print(f"Nickname of {address} is {nickname}")
#         broadcast(f" {nickname} joined the chat!".encode('utf-8'))
#         client.send("Connected to the server!".encode('utf-8'))

#         thread = threading.Thread(target=handle_client, args=(client,))
#         thread.start()


# # --- Start the server ---
# receive_connections()

# ---------------------------------------------------------------------------------------------
# import socket
# import threading

# HOST = '127.0.0.1'
# PORT = 5555

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):
#     for client in clients:
#         try:
#             client.send(message)
#         except:
#             pass

# def handle_client(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             if not message:
#                 break
#             broadcast(message)
#         except:
#             if client in clients:
#                 index = clients.index(client)
#                 nickname = nicknames[index]
#                 clients.remove(client)
#                 nicknames.remove(nickname)
#                 client.close()
#                 broadcast(f"❌ {nickname} left.".encode('utf-8'))
#             break

# def receive_connections():
#     while True:
#         client, address = server.accept()
#         print(f"🟢 Connected with {address}")

#         client.send("NICK".encode('utf-8'))
#         nickname = client.recv(1024).decode('utf-8')

#         nicknames.append(nickname)
#         clients.append(client)

#         print(f"Nickname is {nickname}")
#         broadcast(f"✅ {nickname} joined!".encode('utf-8'))
#         client.send("Connected!".encode('utf-8'))

#         threading.Thread(target=handle_client, args=(client,)).start()

# receive_connections()


# --------------------------------------------------------------------------------------


import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            clients.remove(client)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            broadcast(msg)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat.".encode('utf-8'))
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            break

def receive():
    print(f"Server running on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Name: {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to server!".encode('utf-8'))

        threading.Thread(target=handle, args=(client,)).start()

receive()
