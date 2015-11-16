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
            self.libWebapp()
            self.__connection.close()
            print "Connection close"
    def getHeader(self):
        self.__currentChunk = self.__connection.recv(1)
        self.__receivedMsg = self.__currentChunk
        while self.__currentChunk != '':
            self.__currentChunk = self.__connection.recv(1)
            self.__receivedMsg = self.__receivedMsg + self.__currentChunk
            if "\r\n\r\n" in self__receivedMsg:
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

    def parse_request(self):
        self.__lines = self.__header

        if len(self.__lines) < 1:
            return None
        words = self.__lines.split()
        if len(words) < 3:
            return None
        if words[0] == "GET" or words[0] == "POST" and words[2] in ["HHTP/1.0", "HTTP/1.1"]:
            self.__method = words[0]
            self.__url = words[1]

            if words[0] == "POST":
                self.__contentLenght = self.getContentLenght()
                self.__post_data = ""
                if self.__contentLenght!= 0:
                    self.__data_line = self.getBody()
                    return (self.__method, self.__url, self.__data_line)
                else:
                    return (self.__method, self.__url, [])
            else:
                return None

    def __del__(self):
        self.__mysocket.close()
    def sendResponse(self):
        self.__connection.sendall(self.__response)
    def grades(self):
        return self.__name1, self.__grade1, self.__name2, self.__grade2, self.__name3, self.__grade3, self.__name4, self.__grade4, self.__name5, self.__grade5
    def data(self):
        return self.__data
    def libWebapp(self):
        global o
        self.__response = ""

        self.__header = self.getHeader()
        self.__parameters = self.parse_request()
        parameters = self.__parameters
        if parameters! = None:

            print parameters
            test = parameters[1].split("/")
            test1 = list(test[1])
            test2 = len(test1)
            if test[1] == "" and parameters[0] == "GET":
                self.__data = "GET"
                self.__connection.send("HTTP/1.0 200 OK\n")
                self.__connection.send("Content-Type: text/html\n")
                self.__connection.send("\n")
                self.__connection.send("""
                    <html>
                    <body>
                    <form name="search" action="" method="POST"
                    Name: <input type="text" name="name1"><br><br>
                    Grades: <input type="text" name="grade1"><br><br>
                    Name: <input type="text" name="name2"><br><br>
                    Grades: <input type="text" name="grade2"><br><br>
                    Name: <input type="text" name="name3"><br><br>
                    Grades: <input type="text" name="grade3"><br><br>
                    Name: <input type="text" name="name4"><br><br>
                    Grades: <input type="text" name="grade4"><br><br>
                    Name: <input type="text" name="name5"><br><br>
                    Grades: <input type="text" name="grade5"><br><br>
                    </form>
                    </body>
                    </html>
                    """)
                if test[1] =="" and parameters[0]=="POST":
                    self.__data= "POST"
                    student= parameters[2].split("&")
                    self.__name= student[0].split("name1=")
                    self.__name1= self.__name[1]
                    self.__grade = student[1].split("grade1=")
                    self.__grade1 = self.grade[1]
                    self.__name= student[2].split("name2=")
                    self.__name2= self.__name[1]
                    self.__grade = student[3].split("grade2=")
                    self.__grade1 = self.grade[1]
                    self.__name= student[4].split("name3=")
                    self.__name1= self.__name[1]
                    self.__grade = student[5].split("grade3=")
                    self.__grade1 = self.grade[1]
                    self.__name= student[6].split("name4=")
                    self.__name1= self.__name[1]
                    self.__grade = student[7].split("grade4=")
                    self.__grade1 = self.grade[1]
                    self.__name= student[8].split("name5=")
                    self.__name1= self.__name[1]
                    self.__grade = student[9].split("grade5=")
                    self.__grade1 = self.grade[1]
                    self.__bool = False


                self.sendResponse()







