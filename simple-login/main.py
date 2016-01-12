# coding=utf-8
'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Simple Form

'''

import webapp2  # used the webapp2 library


class MainHandler(webapp2.RequestHandler):  # declaring a class
    def get(self):  # FUNCTION STARTS EVERYTHING

class Page(object):
    def__init__(self):
       self.css = 'css/styles.css'

        # Document heading
        self.head = '''<!DOCTYPE html>
            <html>
             <head>
                <meta charset="UTF-8">
                <title>Student Information Form</title>
            </head>
            <body>

                    '''
        # This will require student information
        self.body = '''
            <div class="logo_wrapper">
                <div class="logo">
                    <img src= "img/logo-dpwp.svg" alt="Logo"></div></div>


            <div id="nav">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Courses</a></li>
                    <li><a href="#">Newsletter</a></li>
                </ul>
            </div>

            <div class="image">
                <img src="img/news-1074604.jpg" alt="&nbsp;">
            </div>

             <div class="header4">
                <h1>Student Newsletter Subscription</h1>
                <h4>If you like to receive our student newsletter, please fill out the form below.</h4>
            </div>

            <div id="section">

            <form method = "GET" id="form">

            <h1 class="form-title">Student Information</h1>
            <label>Name: </label><br><input type="text" name="name" required /><br><br>
            <label>Email: </label><br><input type="text" name="email" required /><br><br>
            <label>Age: </label><br> <input type="text" name="age" required /><br><br>
            <label>University: </label><br><input type="text" name="university" required /><br><br>
            <label>Sex: </label>
             <div class="controls">
                 <input type="radio" name="sex" value="male">Male<br>
                 <input type="radio" name="sex" value="Female">Female<br><br>

            </div>
            <label>Gpa:</label>
            <br><select id="select" name="gpa">
                <option value="From 5.00 to 4.00">From 5.00 to 4.00</option>
                <option value="From 4.00 to 3.00">From 4.00 to 3.00</option>
                <option value="From 3.00 to 2.00">From 3.00 to 2.00</option>
                <option value="From 2.00 to 1.00">From 2.00 to 1.00</option><br><br>
                <input class="button" type="submit" value="Submit">
                '''

        page_close = '''
        </form>
            </div>
                <div id="footer">
                    Copyright © Elimarie Morales Santiago
            </div>
        </body>
        </html>'''

        if self.request.GET:
            # This will store info requested from the form
            name = self.request.GET['name']
            email = self.request.GET['email']
            age = self.request.GET['age']
            sex = self.request.GET['sex']
            university = self.request.GET["university"]
            gpa = self.request.GET['gpa']
            self.response.write(
                'Name:' + name + '<br>Email: ' + email + '<br>Age: ' + age + '<br>Sex: ' + sex + '<br>University:' + university + '<br>Gpa: ' + gpa + '<br><br>' + page_head + page_close)  # this will print output
        else:
            self.response.write(page_head + page_body + page_close)


# VARIABLE THAT RETURN METHOD NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
