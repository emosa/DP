
import webapp2  # used the webapp2 library


class MainHandler(webapp2.RequestHandler):  # declaring a class
    def get(self):  # FUNCTION STARTS EVERYTHING
        # Document heading
       
       response_page = myPage()

        if self.request.GET:
        	self.form_on_submit = true
        	response_page.form_info(self.request.GET)
        else: 
        	self.form_on_submit = false
        	
        	self.response.write(response_page.view(self.form_on_submit))
        	
        	
class myPage(object):
	def __init__(self):
			self.page_title = "Student Information Form"
	def view(self, form_submit):
		if form_submit:
	
            # This will store info requested from the form
            self.name = self.form_info['name']
            self.email = self.form_info['email']
            self.age = self.form_info['age']
            self.sex = self.form_info['sex']
            self.university = self.form_info["university"]
            self.gpa = self.form_info['gpa']
            self.showpage = open('index.html','r').read().format(**locals())
            
            return self.showpage
            
    def form_info(self, data):
    		self.form_info = data
        


# VARIABLE THAT RETURN METHOD NEVER TOUCH IT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
