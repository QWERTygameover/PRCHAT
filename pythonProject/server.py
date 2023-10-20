import socket
from _thread import *


# функция для обработки каждого клиента
def client_thread(con):
    data = con.recv(1024)
    nickname = data.decode()
    while True:
        data = con.recv(1024)  # получаем данные от клиента
        message = data.decode()  # преобразуем байты в строку
        print(f"{nickname}: {message}")
        if message == "":
            con.close()
            break
        for i in clients:
            if i != con:
                i.send(f"{nickname}: {message}".encode())


server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений

clients = []

print("Server running")
while True:
    client, _ = server.accept()  # принимаем клиента
    clients.append(client)
    start_new_thread(client_thread, (client,))  # запускаем поток клиента
