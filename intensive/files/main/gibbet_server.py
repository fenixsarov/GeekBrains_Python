# coding: utf-8

import random
import socketserver

class GibbetTCPHandler(socketserver.BaseRequestHandler):
    """Сервер игры Виселица"""

    def handle(self):
        self.data = self.request.recv(1024).decode()
        print('Клиент {} сообщает {}'.format(self.client_address[0], self.data))

        x = random.randint(1,100)
        # print(x)

        if self.data == 'START':
            self.request.sendall(bytes('GUESS;1;100', 'utf-8'))
            try_count = 10
            while True:
                self.data = self.request.recv(1024).decode()
                resp = self.data.split(';')
                print(resp)
                if resp[0] == 'TRY':
                    if int(resp[1]) == x:
                        self.request.sendall(bytes('TRUE', 'utf-8'))
                        print('Клиент {} выиграл'.format(self.client_address[0]))
                        break
                    else:
                        print('else TRY')
                        try_count -= 1
                        if try_count == 0:
                            self.request.sendall(bytes('FAIL', 'utf-8'))
                            break
                        else:
                           if x < int(resp[1]): 
                                self.request.sendall(bytes('FALSE;{};<'.format(try_count), 'utf-8'))
                           else:     
                                self.request.sendall(bytes('FALSE;{};>'.format(try_count), 'utf-8'))
                elif resp[0] == 'GOODBYE':
                    self.request.sendall(bytes('GOODBYE', 'utf-8'))
                    print('Клиент {} отключился'.format(self.client_address[0]))

                else:
                    print('1 Неизвестный запрос от клиента')                    

        else:
            print('Неизвестный запрос от клиента')



if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999

    server = socketserver.TCPServer((HOST, PORT), GibbetTCPHandler)
    print('Сервер игры "Виселица" запущен')

    server.serve_forever()
