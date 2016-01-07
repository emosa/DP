'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Reusable Library
lib.py
'''


class Grade(object):
    def __init__(  # Constructor for the class to initialize
            self,
            name1,
            grade1,
            name2,
            grade2,
            name3,
            grade3,
            name4,
            grade4,
            name5,
            grade5,
    ):
        self.__name1 = name1  # student name
        self.__grade1 = grade1  # grade value
        self.__name2 = name2
        self.__grade2 = grade2
        self.__name3 = name3
        self.__grade3 = grade3
        self.__name4 = name4
        self.__grade4 = grade4
        self.__name5 = name5
        self.__grade5 = grade5
        self.__list = [
            self.__name1,
            self.__grade1,
            self.__name2,
            self.__grade2,
            self.__name3,
            self.__grade3,
            self.__name4,
            self.__grade4,
            self.__name5,
            self.__grade5,
        ]

    def avg(self):
        self.__lst = [int(self.__grade1), int(self.__grade2),
                      int(self.__grade3), int(self.__grade4),
                      int(self.__grade5)]  # the average will be calculated here
        return sum(self.__lst) / 5

    def median(self):  # Calculate median
        lst = sorted(self.__lst)
        if len(lst) < 1:
            return None
        if len(lst) % 2 == 1:
            return lst[(len(lst) + 1) / 2 - 1]
        else:
            return float(sum(lst[len(lst) / 2 - 1:len(lst) / 2 + 1])) \
                   / 2.0

    def highest(self):  # this will calculate the highest score
        m = max(self.__lst)
        f = self.__list.index(str(m))
        return self.__list[f - 1]
