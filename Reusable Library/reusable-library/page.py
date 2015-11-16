'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Reusable Library
page.py
'''

import socket


class connect():
    def __init__(self):
        port = 8080  # this is my port
        host = "localhost"  # host name
        queue_size = 5
        self.__mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.__mysocket.bind((host, port))
        self.__mysocket.listen(queue_size)
        self.__bool - True
        while self.__bool:
            print "Waiting at http://%s:%d" % (host, port)
            (self.__connection, self.__addr) = self.__mysocket.accept()
