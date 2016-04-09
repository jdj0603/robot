#!/usr/bin/python

import os
import struct
import r_common
import tool_funs

def ls_r(client):
    path = os.getcwd()
    files = tool_funs.traverseDirByOSWalk(path)
    data = ''
    for filename in files:
        data += filename + '\n'
    client.send(data)

def get_r(client, filename):
    filename = filename.strip('\00')
    path = os.getcwd()
    filename = os.path.join(path, filename)

    print [filename]
    err = 0
    size = 0
    if os.path.exists(filename):
        size = os.stat(filename).st_size
    else:
        err = 1

    response = struct.pack(r_common.fmt_file_info, err, size)
    client.send(response)

    if not err:
        amount_sent = 0
        f = open(filename, 'rb')
        while amount_sent < size:
            data = f.read(r_common.BUF_SIZE)
            client.send(data)
            amount_sent += len(data)
        f.close()

def put_r(client, info_data, size):

    filename = 'v:\\new_'+info_data.strip('\00')

    print filename
    f = open(filename, 'wb')

    amount_received = 0

    while amount_received < size:
        data = client.recv(r_common.BUF_SIZE)
        if not info:
            print 'client closed'
            client.close()
            break

        amount_received += len(data)
        print 'received [%d]' % amount_received, 'data'
        f.write(data)

    f.close()
    print 'finished'

if __name__ == '__main__':
    pass
