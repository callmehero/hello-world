# !/usr/bin/python
# -*- coding:utf-8 -*-
import socket

# , ,
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock,addr = server.accept()

while True:
    # 获取从客户端发送的数据
    # 一次获取1k的数据
    data = sock.recv(1024)
    print(data.decode("utf8"))
    something = input("return something: ")
    sock.send("{}".format(something).encode('utf8'))
# server.close()
# sock.close()