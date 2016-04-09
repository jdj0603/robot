#!/usr/bin/python

import socket
import select
import struct
import r_common
import request_handle

# import errno

SERVER_HOST = '127.0.0.1'
SERVER_PORT = int(6666)

class SelectServer(object):
    """A Socket server using select"""

    def __init__(self, host=SERVER_HOST, port=SERVER_PORT):

        self.running = True
        self.count = 0
        self.clients = {}
        self.clients_name = {}
        self.outputs = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind((host, port))

        self.server.listen(100)

        # self.server.setblocking(0)

        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        print "Started Server"

    def run(self):
        """Executer select server operation"""
        inputs = [self.server]

        while self.running:
            print '1'
            try:
                readable, writeable, exceptional = \
                    select.select(inputs, [], [])
            except select.error, e:
                print 'select:error[%s]' % e.message
                break

            for sock in readable:
                print '2'
                if sock == self.server:
                    client, address = self.server.accept()
                    client.setblocking(0)
                    inputs.append(client)
                    # self.outputs.append(client)

                    print 'Client[%s] connected!' % address[0]
                    self.clients[client] = address[0]

                else:
                    print '3'
                    self.recv_data(sock)

    def recv_data(self, client):

        if self.count == 0:

            info_size = struct.calcsize(r_common.fmt_info_head)
            #while True:
            print 'receive info ....'

            info = client.recv(info_size)
            print [info], len(info)

            if not info:
                print 'client[%s] closed' % self.clients[client]
                client.close()
                del self.clients[client]
                return

            cmd, info_data, size = struct.unpack(r_common.fmt_info_head, info)
            print [cmd], [info_data], size

            cmd = cmd.strip('\00')
        else:
            if cmd == 'ls':
                request_handle.ls_r(client)
            elif cmd == 'get':
                request_handle.get_r(client, info_data)
            elif cmd == 'put':
                request_handle.put_r(client, info_data, size)
            else:
                print 'error cmd'

if __name__ == '__main__':
    start()
