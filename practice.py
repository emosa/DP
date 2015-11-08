

'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online

'''

import webapp2   #used the webapp2 library

class MainHandler(webapp2.RequestHandler): #declarin a class
    def get(self): # FUNCTION STARTS EVERYTHING
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"


class Button(object):
    def __init__(self):
        self.label = "" #public attribute
        self __size = 60 #private attribute
        self._color = "0x000" #protected attribute

        #self.on_rollover("Hello")

    def click(self):
        print "I have been clicked"

    def on_rollover(self, message):
        print "You have rolled under my button" + message

    def show_label(self):
        print "MY label is" + self.label





# VARIABLE THAT RETURN METHONG NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

