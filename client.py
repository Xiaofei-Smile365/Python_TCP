# -*- coding: UTF-8 -*-

"""

@author:smile

@file:udp_client.py

@time:2020/10/26

"""

from datetime import datetime  # 导入datetime函数库
import socket  # 导入套接字所需的socket函数库
from threading import Thread  # 导入线程函数库以持续接收数据

address = input("Please input address:\n")

server_address = (address, 8080)  # 设定server端IP和端口
max_size = 1000  # 设定最大缓存

print("Starting the Client at", datetime.now(), "\n")  # 打印客户端欢迎语
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 使用socket建立套接字,使用流协议TCP
client.connect(server_address)  # 建立流

print("Please input in client:")

def recv():
    global client
    while True:
        try:
            data = client.recv(max_size)  # 接收server端数据
            print('At', datetime.now(), 'someone replied [', data.decode("UTF-8"), "] Please input to replied in client:\n")  # 打印接收到的数据
        except:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 使用socket建立套接字,使用流协议TCP
            client.connect(server_address)  # 建立流
            pass
recv_thread = Thread(target=recv)
recv_thread.start()

while True:
    try:
        client_data = input()
        client.sendall(client_data.encode("UTF-8"))  # 向server端发送数据
    except:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 使用socket建立套接字,使用流协议TCP
        client.connect(server_address)  # 建立流
        pass
