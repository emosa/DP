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
                <style type="text/css">
body  {
    font:100%/1.5 Gotham,"Helvetica Neue",Helvetica,Arial,sans-serif;
    color:#FFF;
    width:960px;
    margin:26px auto;
    background:rgba(64,43,0,1);
    background:-moz-linear-gradient(top,rgba(64,43,0,1) 0%,rgba(117,214,255,1) 100%);
    background:-webkit-gradient(left top,left bottom,color-stop(0%,rgba(64,43,0,1)),color-stop(100%,rgba(117,214,255,1)));
    background:-webkit-linear-gradient(top,rgba(64,43,0,1) 0%,rgba(117,214,255,1) 100%);
    background:-o-linear-gradient(top,rgba(64,43,0,1) 0%,rgba(117,214,255,1) 100%);
    background:-ms-linear-gradient(top,rgba(64,43,0,1) 0%,rgba(117,214,255,1) 100%);
    background:linear-gradient(to bottom,rgba(64,43,0,1) 0%,rgba(117,214,255,1) 100%);
    filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#402b00',endColorstr='#75d6ff',GradientType=0)

}
form {
    position:relative;
    margin:50px auto;
    width:480px;
    padding:33px 25px 29px;
    background:#002D40;
    color:#FDFDFD;
    border-bottom:1px solid #75d6ff;
    border-radius:5px
}

form:before,form:after {
    content:'';
    position:absolute;
    bottom:1px;
    left:0;
    right:0;
    height:10px;
    background:inherit;
    border-radius:4px
}
title {
    margin:-25px -25px 25px;
    padding:15px 25px;
    line-height:35px;
    font-size:26px;
    font-weight:300;
    color:#002D40;
    text-align:center;
    text-shadow:1px 1px 0 #ABA2A3;
    background:#75D6FF
}
title:before {
    content:'';
    position:absolute;
    top:0;
    left:0;
    right:0;
    height:8px;
    background:#FFD175;
    border-radius:5px 5px 0 0;
    background-image:-webkit-linear-gradient(left,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805);
    background-image:-moz-linear-gradient(left,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805);
    background-image:-o-linear-gradient(left,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805);
    background-image:linear-gradient(to right,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805)
}
input, #select {
    font-family:inherit;
    color:inherit;
    -webkit-box-sizing:border-box;
    -moz-box-sizing:border-box;
    box-sizing:border-box;
	width:100%;
    height:50px;
    margin-bottom:25px;
    padding:0 15px 2px;
    font-size:17px;
    color:#000;
    background:#fff;
    border:2px solid #ebebeb;
    border-radius:4px;
    -webkit-box-shadow:inset 0 -2px #ebebeb;
    box-shadow:inset 0 -2px #ebebeb;
    line-height:48px
}

.controls input {
    display: inline-block;
    width: 40px;
    height: 20px;
    text-align: center;
    vertical-align: top;
    padding-top: 20px;
    margin: 0 auto 5px;
}

.button {
    width: 100%;
    text-align:center  !important;
    cursor:pointer;
    background:#23A3DA;
    background-image:-webkit-linear-gradient(top,#23A3DA,#03171F);
    background-image:-moz-linear-gradient(top,#23A3DA,#03171F);
    background-image:-ms-linear-gradient(top,#23A3DA,#03171F);
    background-image:-o-linear-gradient(top,#23A3DA,#03171F);
    background-image:linear-gradient(to bottom,#23A3DA,#03171F);
    -webkit-border-radius:5;
    -moz-border-radius:5;
    border-radius:5px;
    -webkit-box-shadow:1px 1px 1px #666;
    -moz-box-shadow:1px 1px 1px #666;
    box-shadow:1px 1px 1px #666;
    font-family:Arial;
    color:#fff;
    font-size:25px;
    padding:2px 10px 10px 10px;
    text-decoration:none
}

.button:hover {
    background:#E3A019;
    background-image:-webkit-linear-gradient(top,#E3A019,#E3A019);
    background-image:-moz-linear-gradient(top,#E3A019,#E3A019);
    background-image:-ms-linear-gradient(top,#E3A019,#E3A019);
    background-image:-o-linear-gradient(top,#E3A019,#E3A019);
    background-image:linear-gradient(to bottom,#E3A019,#E3A019);
    text-decoration:none
}

.form-title {
    margin:-25px -25px 25px;
    padding:15px 25px;
    line-height:35px;
    font-size:26px;
    font-weight:300;
    color:#002D40;
    text-align:center;
    text-shadow:1px 1px 0 #ABA2A3;
    background:#75D6FF
}

.form-title:before {
    content:'';
    position:absolute;
    top:0;
    left:0;
    right:0;
    height:8px;
    background:#FFD175;
    border-radius:5px 5px 0 0;
    background-image:-webkit-linear-gradient(left,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805);
    background-image:-moz-linear-gradient(left,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805);
    background-image:-o-linear-gradient(left,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805);
    background-image:linear-gradient(to right,#8d6109,#8d6109 12.5%,#ffd175 12.5%,#ffd175 25%,#09668d 25%,#09668d 37.5%,#ffd175 37.5%,#ffd175 50%,#23a3da 50%,#23a3da 62.5%,#402b00 62.5%,#402b00 75%,#ffd175 75%,#ffd175 87.5%,#9a6805 87.5%,#9a6805)
}

    </style>
            </head>
            <body>

                    '''
        # This will require student information
        page_body = '''


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
