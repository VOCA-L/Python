import socket
import json 
from enum import Enum

# server IP, PORT
HOST = '127.0.0.1'
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def Command(Enum):
    START = 1
    RUNNING = 2
    STOP = 3

while True:
    header
    body

    command = input("Enter your command\n")
    command = Command[command]

# message
di = {}
di["name"] = "Hamji"
di["old"] = 27
body = json.dumps(di)

leng = len(body)

message = bytearray(header)
## 보낼 때는 python 3.1 ~에서 슬 수 있는 .to_bytes사용 
message += bytearray(leng.to_bytes(2, byteorder="big"))
message += bytes(body,'utf-8')
print("send Message: ",message)

client_socket.sendall(message)

data = client_socket.recv(1024)
print('Server Received my Message~!')
client_socket.close()