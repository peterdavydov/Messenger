import socket
import time

HOST = "127.0.0.1"
PORT = 12345
FORMAT = "utf-8"

class Client:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
    
    def connect(self):
        self.login = input("Login: ")
        self.password = input("Password: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        self.send_messege(self.login)
        self.send_messege(self.password)
        self.check_connection = True
    
    def send_messege(self, messege):
        self.check_connection = not(messege == "DISCONNECT")
        msg_out = messege.encode(FORMAT)
        self.client.send(msg_out)
        time.sleep(1)

    def get_message(self):
        self.msg = self.client.recv(1024).decode(FORMAT)
        print("Server:", self.msg)
    

client = Client(HOST, PORT)
client.connect()
while client.check_connection:
    client.send_messege(input("You: "))
    if client.check_connection:
        client.get_message()
