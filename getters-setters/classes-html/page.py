
"""
ELIMARIE MORALES SANTIAGO
FULL SAIL UNIVERSITY
Design Patterns for Web Programming - Online
classes-getter-setter

"""

class Page(object):
    def __init__(self):
        self.__title = "Fixed Welcome!"
        self.__css = "css/styles.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>(self.title)</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        """

        self.__body = "Welcome to my page"
        self.close = """
    </body>
</html>
        """
        self.whole_page = ""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file
        self.update()

