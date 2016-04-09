#!/usr/bin/python

import os
import socket
import struct
import argparse
import tools as t


p = 'v:\\'

g_cmd = ''
while g_cmd:
    g_cmd = raw_input('>')
    gp = t.get_cmd_group(g_cmd)
    if gp[0] == 'ls':
        a1 = os.listdir(p)
        for i in a1:
            print i

    elif gp[0] == 'del':
        pp = p + gp[1]
        print pp
        os.remove(pp)

    elif gp[0] == 'read':
        f = open(p + gp[1], 'r')
        for eachLine in f:
            print eachLine,

    elif gp[0] == 'dir':
        t.traverseDirByOSWalk(p)

    elif gp[0] == 'time':
        t.show_time(int(gp[1]))

    elif gp[0] == 'pack':
        fmt = '4s8si'

        fhead = struct.pack(fmt, '1001', 'test', 88)
        num, name, size = struct.unpack(fmt, fhead)
        print [num]
        print [name]
        print [size]

    elif gp[0] == 'pipe':
        var = os.popen(gp[1]).read()
        print var
    elif gp[0] == 'host':
        host = socket.gethostname()
        print host
    elif gp[0] == 'ip':
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        print ip
    elif gp[0] == 'exit':
        print 'exit'
    else:
        print 'error cmd'

if __name__ == '__main__':
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    parse = argparse.ArgumentParser()
    parse.add_argument('-ip', default=ip, required=False)
    given_args = parse.parse_args()
    print given_args.ip
