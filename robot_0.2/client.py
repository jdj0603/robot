#!/usr/bin/python

import socket
import client_command
import tool_funs

def start():

    #host = socket.gethostname()
    port = int(6666)

    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

    s_addr = ('127.0.0.1', port)

    sock.connect(s_addr)

    cmd = ''
    while cmd != 'exit':

        cmd = raw_input('>')
        gp = tool_funs.get_cmd_group(cmd)

        if gp[0] == 'ls':
            client_command.ls(sock)

        elif gp[0] == 'get':
            client_command.get(sock, gp[1])

        elif gp[0] == 'put':
            client_command.put(sock, gp[1])

        elif gp[0] == 'bye':
            break

    sock.close()


if __name__ == '__main__':
    start()
