import os
import socket

from Crypto.Cipher import AES

key = b"TheNeuralNinekey"
nonce=b"TheNeuralNineNce"

cipher = AES.new(key,AES.MODE_EAX,nonce)

cipher=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))

file_size = os.path.getsize("file")

with open("file","rb") as f:
    data = f.read()

encrypted=cipher.encrypt(data)
client.send("file.txt".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<END>")

client.close()