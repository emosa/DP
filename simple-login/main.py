"""
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Simple Form

"""

import webapp2  # used the webapp2 library
from page import Page


class MainHandler(webapp2.RequestHandler):

        def get(self):
            page = Page()   # Creates an instance of the imported class page

            if self.request.GET:     # Check if GET exists
                # Get form data from url
                name = self.request.GET['name']
                email = self.request.GET['email']
                university = self.request.GET['university']
                degree = self.request.GET['degree']
                interest = self.request.GET["interest"]
                gpa = self.request.GET['gpa']

                display = '''
                <!DOCTYPE>
                <html>
                   <head>
                      <title>Student Newsletter Confirmation Page</title>
                      <link type="text/css" rel="stylesheet" href="css/styles.css"/>
                   </head>
                   <body>

                 <div class="logo_wrapper">
                 <div class="logo">
                  <img src= "img/logo-dpwp.svg" alt="Logo"></div></div>

                 <div id="nav">
                  <ul>
                    <li><a href="#" title="Home"><span>Home</span></a></li>
                    <li><a href="#" title="Courses"><span>Courses</span></a></li>
                    <li><a href="#" title="Newsletter"><span>Newsletter</span></a></li>
                  </ul>
                </div>

                 <div class="image">
                    <img src="img/news-1074604.jpg" alt="worldnews">
                 </div>
                 <div class="display">

                    <h1><font size="6" color="#065F98">Newsletter Confirmation</font></h1>
                    <p><font size="4" color="#92b749">You name is {name}, student at {university}.
                    You have a degree on {degree}, with a average GPA of {gpa}. Your email address is: {email},
                    and your technology of interest is {interest}. </p></font>
                    <p><font size="4" color="#065F98">Thank you for subscribing to our newsletter.</font></p>
                    <p> </p>

                 </div>
                    '''

                display = display.format(**locals())
                # print form content
                self.response.write(page.header + display + page.footer)

            else:
                self.response.write(page.header + page.body + page.footer)

# VARIABLE THAT RETURN METHOD NEVER TOUCH IT
app = webapp2.WSGIApplication({
    ('/', MainHandler)
}, debug=True)
