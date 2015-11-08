'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Simple Form

'''

import webapp2  # used the webapp2 library


class MainHandler(webapp2.RequestHandler):  # declaring a class
    def get(self):  # FUNCTION STARTS EVERYTHING
        # Document heading
        page_head = '''<!DOCTYPE html>
            <html>
             <head>
                <meta charset="UTF-8">
                <title>Student Information Form</title>
            </head>
            <body>
                    '''
        # This will require student information
        page_body = '''

        <form method = "GET" >
            <label>Name: </label><br><input type="text" name="name" /><br><br>
            <label>Email: </label><br><input type="text" name="email" /><br><br>
            <label>Age: </label><br> <input type="text" name="age" /><br><br>
            <label>Sex: </label><br>
                        <input type="radio" name="sex" value="male">Male
                        <input type="radio" name="sex" value="Female">Female<br><br>
            <label>Gpa:</label>
            <br><select name="gpa">
                <option value="From 5.00 to 4.00">From 5.00 to 4.00</option>
                <option value="From 4.00 to 3.00">From 4.00 to 3.00</option>
                <option value="From 3.00 to 2.00">From 3.00 to 2.00</option>
                <option value="From 2.00 to 1.00">From 2.00 to 1.00</option>
                    <input type="submit" value="Submit">'''
        page_close = '''
        </form>
            </body>
            </html>'''

        if self.request.GET:
            # This will store info requested from the form
            name = self.request.GET['name']
            email = self.request.GET['email']
            age = self.request.GET['age']
            sex = self.request.GET['sex']
            gpa = self.request.GET['gpa']
            self.response.write(
                'Name:' + name + '<br>Email: ' + email + '<br> Age: ' + age + '<br>Sex: ' + sex + '<br>Gpa: ' + gpa + '<br><br>' + page_head + page_body + page_close)  # this will print output
        else:
            self.response.write(page_head + page_body + page_close)


# VARIABLE THAT RETURN METHOD NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
