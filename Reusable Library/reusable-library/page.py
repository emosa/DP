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
        self.__bool = True
        while self.__bool:
            print "Waiting at http://%s:%d" % (host, port)
            (self.__connection, self.__addr) = self.__mysocket.accept()
            print "New connections", self.__connection, self.__addr
            self.fridayWebapp()
            self.__connection.close()
            print "Connection close"
    def getHeader(self):
        self.__currentChunk = self.__connection.recv(1)
        self.__receivedMsg = self.__currentChunk
        while self.__currentChunk != '':
            self.__currentChunk = self.__connection.recv(1)
            self.__receivedMsg = self.__receivedMsg + self.__currentChunk
            if "r/m/r/n" in self__receivedMsg:
                break
        return self.__receivedMsg
    def getContentLenght(self):
        self.__lines = self.__header.split("\r\n")
        for line in self.__lines:
            if "Content-Lenght:" in line:
                s = line.split(":")
                return int([1])
            return 0
    def getBody(self):
        return self.__connection.recv(self.contentLenght)
    def send(self,a,b,c):
        self.__connection.send("HTTP/1.0 200 OK\n")
        self.__connection.send("Content-Type: text/html\n")
        self.__connection.send("\n")
        self.__connection.send("Average=" + str(a))
        self.__connection.send("\n")
        self.__connection.send("\nMedian=" + str(b))
        self.__connection.send("\n")
        self.__connection.send("\nHighest Score=" + str(c))








