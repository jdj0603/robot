#!/usr/bin/python

import threading
import r_server


def start():
    server = r_server.SelectServer()
    server_thread = threading.Thread(target=server.run, args=())
    server_thread.start()
    server_thread.join()

if __name__ == '__main__':
    start()
