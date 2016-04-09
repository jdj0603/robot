#!/usr/bin/python

import os
import time


def get_cmd_group(cmd):
    gp = cmd.split(' ')
    gp_r = []
    for g in gp:
        if g != '':
            gp_r.append(g)
    return gp_r


def traverseDirByOSWalk(path):
    files = []
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        print('[' + dirname + ']')
        files.append(dirname)
        for f in subfile:
            fullname = os.path.join(dirname, f)
            print(fullname)
            files.append(fullname)
    return files


def show_time(time_n=10):
    while time_n:
        print time.strftime('%Y-%m-%d %H:%M:%S')+'\r',
        time.sleep(1)
        time_n -= 1
    print '\n',


if __name__ == '__main__':
    pass
