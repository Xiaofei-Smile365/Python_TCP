# -*- coding: UTF-8 -*-

"""

@author:smile

@file:udp_server.py

@time:2020/10/26

"""

from datetime import datetime  # 导入datetime函数库
import socket  # 导入套接字所需的socket函数库
from threading import Thread  # 导入线程函数库以持续接收数据

address = input("Please input address:\n")

server_address = (address, 8080)  # 设定server端IP和端口
max_size = 1000  # 设定最大的可接收消息长度为1000字节

print("Starting the server at", datetime.now())  # 打印server端欢迎语
print("Waiting for a client to call", "\n")  # 打印等待客户端连接
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 使用socket建立套接字
server.bind(server_address)  # 绑定到相应IP&端口
server.listen(1)  # 最多和5个客户端保持连接
client, addr = server.accept()  # 接收第一个到达的消息

print("Please input in server:")

def recv():
    global client, addr
    while True:
        try:
            data = client.recv(max_size)  # 接收客户端数据
            print("At", datetime.now(), "someone said [", data.decode("UTF-8"), "] Please input to replied in server:\n")  # 打印接收到的数据
        except:
            client, addr = server.accept()  # 接收第一个到达的消息
            pass
recv_thread = Thread(target=recv)
recv_thread.start()

while True:
    try:
        server_data = input()
        client.sendall(server_data.encode("UTF-8"))  # 回应客户端数据
    except:
        client, addr = server.accept()  # 接收第一个到达的消息
        pass

