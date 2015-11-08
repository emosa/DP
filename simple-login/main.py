

'''
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Simple Form

'''

import webapp2   #used the webapp2 library

class MainHandler(webapp2.RequestHandler): #declarin a class
    def get(self): # FUNCTION STARTS EVERYTHING
            #Document heading
        page_head = '''
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <meta charset="UTF-8">
                    <title>Patient Information Form</title>
                    </head>
                    <body>
                    '''
            #This will require student information
        page_body = '''
                    <form method = "GET" >
                    Name: <br><input type="text" name="name" /><br><br>
                    Email: <br><input type="text" name="email" /><br><br>
                    Age: <br> <input type="text" name="age" /><br><br>
                    Sex: <br> <input type="radio" name="sex" value="male">Male <input type="radio" name="sex" value="Female"<br><br>
                    Gpa:
                        <br> select name="gpa">
                          <option value="From 5.00 to 4.00">From 5.00 to 4.00</option>
                          <option value="From 4.00 to 3.00">From 4.00 to 3.00</option>
                          <option value="From 3.00 to 2.00">From 3.00 to 2.00</option>
                          <option value="From 2.00 to 1.00">From 2.00 to 1.00</option>
                    <input type="submit" value="Submit">'''
        page_close = '''
                     </form>
                     </body>
                     </html>'''

        if self.request.Get:
            #This will store info requested from the form
            name=self.request.GET['name']
            email=self.request.GET['email']
            age=self.request.GET['age']
            sex=self.request.GET['gpa']









# VARIABLE THAT RETURN METHONG NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

