#!/usr/bin/python

import socket
import struct
import common
import request_handle
# import errno


def start():

    host = socket.gethostname()

    port = int(12345)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s_addr = (host, port)

    sock.bind(s_addr)

    sock.listen(1)

    running = True

    while running:

        print 'wait client connect...'

        client, ip = sock.accept()
        print 'client connected!'

        running = recv_data(client)
        print running



def recv_data(client):

    info_size = struct.calcsize(common.fmt_info_head)

    while True:
        print 'receive info head....'

        info = client.recv(info_size)
        print [info], len(info)

        if not info:
            print 'client closed'
            client.close()
            break

        cmd, info_data, size = struct.unpack(common.fmt_info_head, info)
        print [cmd], [info_data], size

        cmd = cmd.strip('\00')
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
    start()
