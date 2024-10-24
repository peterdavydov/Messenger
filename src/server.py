import socket
import json
import time

HOST = "127.0.0.1"
PORT = 12345
FORMAT = "utf-8"

class Server:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def run_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
    
    def stop_connection_user(self):
        self.connection = False
        self.conn.close()

    def stop_server(self):
        self.server.close()

    def get_connection_user(self):
        self.server.listen(1)
        self.conn, self.addr = self.server.accept()
        self.login = str(self.conn.recv(1024).decode(FORMAT))
        self.password = str(self.conn.recv(1024).decode(FORMAT))
        self.connection = True
        with open("data/passwords.json", encoding="UTF-8") as file:
            data = json.load(file)
            if self.login in data and data[self.login] == self.password:
                print(f"Connect User with name {self.login}")
            else:
                self.connection = False
                self.stop_connection_user()
    
    def get_message(self):
        self.msg = self.conn.recv(1024).decode(FORMAT)
        print(f"{self.login}:", self.msg)

    def send_messege(self, messege):
        msg_out = messege.encode(FORMAT)
        self.conn.send(msg_out)
        time.sleep(1)
    
    def check_connection(self):
        if self.msg == "DISCONNECT":
            self.stop_connection_user()


server = Server(HOST, PORT)
server.run_server()
server.get_connection_user()
while server.connection:
    server.get_message()
    server.check_connection()
    if server.connection:
        server.send_messege(input("You: "))
server.stop_connection_user()
server.stop_server()
