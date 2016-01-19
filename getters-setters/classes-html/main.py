"""
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
classes-getter-setter

"""

import webapp2  # used the webapp2 library
from page import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()   # Creates an instance of the imported class page
        page.title = "Title"
        page.css = "css/styles.css"
        page.body = "Miss piggy"
        page.update()
        self.response.write(page.whole_page)



#VARIABLE THAT RETURN METHOD NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
