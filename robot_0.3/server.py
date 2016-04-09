#!/usr/bin/python

import socket
import argparse
import struct
import common
import request_handle
# import errno

SERVER_HOST = 'localhost'
SERVER_PORT = int(6666)


class RServer(object):

    def __init__(self, host=SERVER_HOST, port=SERVER_PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        print 'Server Started'
        self.clients = {}

    def run(self):
        running = True

        while running:
            client, ip = self.sock.accept()
            print '[%s] connected!' % ip[0]
            self.clients[client] = ip[0]

            running = self.recv_data(client)

    def recv_data(self, client):

        info_size = struct.calcsize(common.fmt_info_head)
        while True:
            info = client.recv(info_size)
            # print [info], len(info)

            if not info:
                print '[%s] closed!' % self.clients[client]
                client.close()
                break

            cmd, info_data, size = struct.unpack(common.fmt_info_head, info)
            # print [cmd], [info_data], size

            cmd = cmd.strip('\00')
            print 'Got client cmd:[%s]' % cmd
            if cmd == 'ls':
                request_handle.ls_r(client)
            elif cmd == 'get':
                request_handle.get_r(client, info_data)
            elif cmd == 'put':
                request_handle.put_r(client, info_data, size)
            elif cmd == 'stop':
                client.close()
                return False
            else:
                print 'error cmd'

        return True

if __name__ == '__main__':
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    parse = argparse.ArgumentParser()
    parse.add_argument('-ip', default=ip, required=False)
    parse.add_argument('-port', default=SERVER_PORT, type=int, required=False)
    given_args = parse.parse_args()

    print 'ip:[%s] port:[%d]' % (given_args.ip, given_args.port)
    server = RServer(given_args.ip, given_args.port)
    server.run()
