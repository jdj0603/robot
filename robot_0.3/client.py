#!/usr/bin/python

import socket
import argparse
import client_command
import tool_funs

SERVER_PORT = int(6666)


class RClient(object):
    def __init__(self, host, port):

        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        s_addr = (host, port)
        self.sock.connect(s_addr)

    def run(self):
        while True:
            cmd = raw_input('>')
            if cmd:
                gp = tool_funs.get_cmd_group(cmd)

                if gp[0] == 'ls':
                    client_command.ls(self.sock)

                elif gp[0] == 'get':
                    client_command.get(self.sock, gp[1])

                elif gp[0] == 'put':
                    client_command.put(self.sock, gp[1])

                elif gp[0] == 'bye':
                    break

                elif gp[0] == 'stop':
                    client_command.stop(self.sock)
                    break

        self.sock.close()


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-ip', default='192.168.1.105', required=False)
    parse.add_argument('-port', default=SERVER_PORT, type=int, required=False)
    given_args = parse.parse_args()

    print 'ip:[%s] port:[%d]' % (given_args.ip, given_args.port)

    rclient = RClient(given_args.ip, given_args.port)
    rclient.run()
