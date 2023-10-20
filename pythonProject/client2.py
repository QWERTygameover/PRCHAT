import socket
from _thread import *

client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client.connect((hostname, port))  # подключаемся к серверу

message = ""

nickname = input("Введите ник")
client.send(nickname.encode())

datas = []


def TakeMsg():
    while True:
        data = client.recv(1024)
        print(data.decode())


def SendMsg():
    while True:
        message = input("")  # вводим сообщение
        client.send(message.encode())  # отправляем сообщение серверу


start_new_thread(TakeMsg, ())
start_new_thread(SendMsg, ())

while True:
    a = 1