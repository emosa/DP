
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() # This needs to refer to the submost class you are wanting to use
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out_form())

class Page(object):  # Borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = "filler"
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self): #Constructor function for super class
        Page.__init__(self)
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        # <input type="text" value="" name="first_name" placeholder="First Name" />
        # ['first_name', 'text', 'First Name']
        # <input type="text" value="" name="last_name" placeholder="Last Name" />
        # <input type="submit" value="Submit"/>

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        # sort through the mega array and create HTML inputs based on info there.
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            # If there is a 3rd Item, add it in
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            # Otherwise end the tag.
            except:
                self._form_inputs += '" />'

        print self._form_inputs

    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

    """ other code """

    class Player:
        def __init__(self):
            self.__playlist = []

        def play(self):
        #code for playing audio and video

    class AudioPlayer(Player):
        def __init__(self):
            super(AudioPlayer, self).__init__()

        def play(self):
        #code for playing ONLY audio override the top def play


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
