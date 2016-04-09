#/usr/bin/env python

import os
import struct
import tools as t

#from PIL import ImageGrab



p = 'v:\\'

g_cmd = ''
while g_cmd != 'exit':
    g_cmd = raw_input('>')
    gp = t.get_cmd_group(g_cmd)
    if gp[0] == 'ls':
        a1 =  os.listdir(p)
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
    elif gp[0] == 'exit':
        print 'exit'
    else:
        print 'error cmd'