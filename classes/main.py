
import webapp2  # used the webapp2 library


class MainHandler(webapp2.RequestHandler):  # declaring a class
    def get(self):  # FUNCTION STARTS EVERYTHING
       self.response.write('Hello World')

class Button(object):
    def __init__(self):
        pass

    def click(self):
        pass






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)