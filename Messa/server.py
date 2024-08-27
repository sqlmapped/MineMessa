import socket
import threading

pcip = input("use PC's IP? (y/n): ").lower() == 'y' # using you ip for connection
ip = socket.gethostbyname(socket.gethostname()) if pcip else input("enter IP: ")
port = 4422 if use_pcip else int(input("Enter Port: "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(5)
print(f"your IP for connection: {ip}:{port}. please update IP in client.lua.") #

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            if msg:
                print(f"> user: {msg}") # for read message
                client_socket.send("message received".encode("utf-8"))
        except:
            client_socket.close()
            break

while True:
    client_socket, _ = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket,)).start()
