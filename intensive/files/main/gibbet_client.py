# coding: utf-8

import socket
import sys

HOST = 'localhost'
PORT = 9999

print('Клиент игры Виселица')
print('Подключение к {}:{}...'.format(HOST,PORT))

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
except:
    print('Ошибка подключения к серверу!')    
    sys.exit(13)

print('Отправка START')
try:
    sock.sendall(bytes('START', 'utf-8')) 
    received = sock.recv(1024).decode()
except:
    print('Ошибка отправки данных на сервер!')       
    sock.close()

data = received.split(';') 
print(data)   

if data[0] == 'GUESS':
    print('Угадайте число от {} до {}'.format(data[1], data[2]))

    while True:
        x = input('Ваш ответ (q - для выхода): ')  # raw_input()
        if x == 'q':
            sock.sendall(bytes('GOODBYE', 'utf-8'))
            break

        try:
            sock.sendall(bytes('TRY;{}'.format(x), 'utf-8'))
            received = sock.recv(1024).decode()
        except:
            print('Ошибка отправки числа серверу')    
            break

        # print('Сервер ответил: {}'.format(received))
        data = received.split(';')    
        if data[0] == 'TRUE':
            print('Вы угадали!')
            break
        elif data[0] == 'FALSE':
            if data[2] == '<':
                print('Вы не угадали. Число меньше. У Вас осталось попыток: {}'.format(data[1]))
            else:           
                print('Вы не угадали. Число больше. У Вас осталось попыток: {}'.format(data[1]))
        elif data[0] == 'FAIL':
            print('Вы не угадали число и проиграли! :(')
            break
else:
    print('Неизвестный ответ сервера')

sock.close()        







