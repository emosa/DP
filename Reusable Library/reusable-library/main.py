'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Reusable Library
mainHandler.py
'''

import webapp2
import page
import lib

class MainHandler(webapp2.RequestHandler):

    c = page.connect()  #  This will create object for connect class
while True:
    if 'POST' == c.data():
        grades = c.grades()  # Obtaining data
        cal = lib.Grade(  # This will send data to constructor
            grades[0],
            grades[1],
            grades[2],
            grades[3],
            grades[4],
            grades[5],
            grades[6],
            grades[7],
            grades[8],
            grades[9],
            )
        a = cal.avg()  # Get average
        b = cal.median()  # Get median
        _c = cal.highest()  # Get highest score
        c.send(a, b, _c)  # send info
        break



# VARIABLE THAT RETURN METHOD NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
