# coding=utf-8
"""
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
Simple Form

"""

class Page(object):
    def __init__(self):
        self.header = '''<!DOCTYPE html>
                <html>
                   <head>
                      <title>Student Newsletter Subscription Form</title>
                      <link type="text/css" rel="stylesheet" href="css/styles.css"/>
                   </head>
                   <body>
                    '''

        self.body = '''
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

                <div class="header4">
                  <h1>Student Newsletter Subscription</h1>
                  <h4>If you like to receive our student newsletter, please fill out the form below.</h4>
                </div>

                <div id="section">


                 <form method = "GET" id="form">

                 <h1 class="form-title">Student Information</h1>
                     <label>Name: </label><br><input type="text" name="name" required /><br><br>
                     <label>Email: </label><br><input type="text" name="email" required /><br><br>
                     <label>University: </label><br><input type="text" name="university" required /><br><br>
                     <label>Degree: </label><br> <input type="text" name="degree" required /><br><br>
                     <label>Technologies of interests: </label><br><br>
                 <div class="controls">
                     <input type="radio" name="interest" value="Python">Python<br>
                     <input type="radio" name="interest" value="PHP">PHP<br>
                     <input type="radio" name="interest" value="HTML">HTML<br><br>
                 </div>

                     <label>Gpa:</label>
                       <br><select id="select" name="gpa">
                       <option value="From 5.00 to 4.00">From 5.00 to 4.00</option>
                       <option value="From 4.00 to 3.00">From 4.00 to 3.00</option>
                       <option value="From 3.00 to 2.00">From 3.00 to 2.00</option>
                       <option value="From 2.00 to 1.00">From 2.00 to 1.00</option></select><br><br>
                    <input class="button" type="submit" value="Submit">
                 </form>
                 </div>

                 '''

        self.footer = '''
                   </body>
                       <div id="footer">
                       <p> Copyright © Elimarie Morales Santiago </p>
                 </div>
                 </html>
                 '''
# methods to define page content and get data
    def header(self):
        return self.header

    def form(self):
        return self.body

    def footer(self):
        return self.footer
