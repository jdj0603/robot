#!/usr/bin/python

import os
import struct
import r_common

def ls(sock):
    info_head = struct.pack(r_common.fmt_info_head, 'ls', '', 0)
    sock.send(info_head)
    data = sock.recv(r_common.BUF_SIZE)
    if data:
        print data
    else:
        print 'server is closed'


def get(sock, filename):
    info_head = struct.pack(r_common.fmt_info_head, 'get', filename, 0)
    sock.send(info_head)

    size = struct.calcsize(r_common.fmt_file_info)
    size = sock.recv(size)
    err, size = struct.unpack(r_common.fmt_file_info, size)

    print err, size

    if err != 0:
        print 'The file [%s]' % filename + ' is not exist on the server'
        return

    filename = 'v:\\New_server_' + filename
    print filename
    f = open(filename, 'wb')

    amount_received = 0
    while amount_received < size:
        data = sock.recv(r_common.BUF_SIZE)
        if not data:
            print 'server is closed'
            break

        f.write(data)
        amount_received += len(data)
        print 'received [%d]' % amount_received, 'data'

    f.close()

def put(sock, filename):

    file_size = os.stat(filename).st_size

    info_head = struct.pack(r_common.fmt_info_head, 'put', os.path.basename(filename), file_size)
    print len(info_head)
    sock.send(info_head)

    amount_sent = 0
    f = open(filename, 'rb')
    while amount_sent < file_size:
        data = f.read(r_common.BUF_SIZE)
        print [data]
        if not data:
            break
        sock.send(data)
        amount_sent += len(data)
        rate = amount_sent * 100 / file_size
        print 'received [%d%%]' % rate

    print '\n'
    f.close()

if __name__ == '__main__':
    pass
