

'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Simple Form

'''

import webapp2   #used the webapp2 library

class MainHandler(webapp2.RequestHandler): #declarin a class
    def get(self): # FUNCTION STARTS EVERYTHING

        page_head = '''
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <meta charset="UTF-8">
                    <title>Patient Information Form</title>
                    </head>
                    <body>
                    '''




# VARIABLE THAT RETURN METHONG NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

