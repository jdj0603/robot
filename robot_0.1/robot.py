#!/usr/bin/python

import server
import threading


def start():
    server_thread = threading.Thread(target=server.start, args=())
    server_thread.start()
    server_thread.join()


if __name__ == '__main__':
    start()
