# import socket
# import threading

# # --- Client Configuration ---
# HOST = '127.0.0.1'
# PORT = 5555

# nickname = input("Enter your nickname: ")

# # --- Create socket and connect to server ---
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, PORT))


# # --- Receive messages continuously ---
# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             if message == "NICK":
#                 client.send(nickname.encode('utf-8'))
#             else:
#                 print(message)
#         except:
#             print(" Connection lost!")
#             client.close()
#             break


# # --- Send messages continuously ---
# def write():
#     while True:
#         message = f"{nickname}: {input('')}"
#         client.send(message.encode('utf-8'))


# # --- Start both threads ---
# threading.Thread(target=receive).start()
# threading.Thread(target=write).start()


# ------------------------------------------------------------------------------------

# import socket
# import threading

# HOST = '127.0.0.1'
# PORT = 5555

# nickname = input("Enter nickname: ")

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, PORT))

# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             if message == "NICK":
#                 client.send(nickname.encode('utf-8'))
#             else:
#                 print(message)
#         except:
#             print(" Connection lost!")
#             client.close()
#             break

# def write():
#     while True:
#         message = f"{nickname}: {input('')}"
#         client.send(message.encode('utf-8'))

# threading.Thread(target=receive).start()
# threading.Thread(target=write).start()



# ----------------------------------------------------------------

import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Connection closed!")
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input('')}"
        client.send(msg.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
