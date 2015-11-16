'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Reusable Library
mainHandler.py
'''

import page, lib

c = page.connect()  # This will create object for connect class
while True:
    if c.data() == "POST":
        grades = c.grades()  # Obtaining data
        cal = lib.Grade(grades[0], grades[1], grades[2], grades[3], grades[4], grades[5], grades[6], grades[7],
                        grades[8], grades[9])  # This will send data to constructor
        a = cal.avg()  # Get average
        b = cal.median()  # Get median
        _c = cal.highest()  # Get highest score
        c.send(a, b, _c)  # Send info
        break
