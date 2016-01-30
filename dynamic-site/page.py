# coding=utf-8
"""
# ELIMARIE MORALES SANTIAGO
# FULL SAIL UNIVERSITY
# Design Patterns for Web Programming - Online
# Dynamic Site
"""


class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
          <title>Gemstone Treasures</title>
          <link href="css/styles.css" rel="stylesheet" type="text/css">
    </head>

    <body>
        '''
        self._body = '''
        <div class="logo_wrapper">
        <div class="logo">
            <img src="img/logo.png" alt="Logo"></div>
        </div>
            <ul id="nav">
                <li><a href="?name=opal">Opal</a></li>
                <li><a href="?name=amethyst">Amethyst</a></li>
                <li><a href="?name=diamond">Diamond</a></li>
                <li><a href="?name=topaz">Topaz</a></li>
                <li><a href="?name=tourmaline">Tourmaline</a></li>
            </ul>
        '''
        self._footer = '''
            <footer>
               <div id="footer">
                     Copyright © EMS Gemstone Treasures
               </div>
            </footer>
    </body>
</html>
        '''

    # method define content and print data
    def print_out(self):
        return self._head + self._body + self._close


# class holding the attributes for page content"""
class GemstonePage(Page):
    def __init__(self):
        super(GemstonePage, self).__init__()
        self._div_content = '<div class="gems">'
        self._div_end = '</div>'
        self._name = ''
        self._img = ''
        self._bio = ''
        self._origin = ''
        self._story = ''
        self._locations = ''
        self._colors = ''

    # Getters """
    @property
    def name(self):
        return self.__name

    @property
    def img(self):
        return self.__img

    @property
    def bio(self):
        return self.__bio

    @property
    def origin(self):
        return self.__origin

    @property
    def story(self):
        return self.__story

    @property
    def locations(self):
        return self.__locations

    @property
    def colors(self):
        return self.__colors

    # Setters """

    @name.setter
    def name(self, gem_name):
        self._name = gem_name

    @img.setter
    def img(self, gem_img):
        self._img = gem_img

    @bio.setter
    def bio(self, gem_bio):
        self._bio = gem_bio

    @origin.setter
    def origin(self, gem_origin):
        self._origin = gem_origin

    @story.setter
    def story(self, gem_story):
        self._story = gem_story

    @locations.setter
    def locations(self, gem_locations):
        self._locations = gem_locations

    @colors.setter
    def colors(self, gem_colors):
        self._colors = gem_colors

    # print content overwrite print on page class
    @property
    def print_out(self):
        return self._head + self._body + self._div_content + '<h1>' + self._name + '</h1>' + '<h2>' + self._bio + '</h2>' + '<div class="image"><img src="' + self._img + '"/></div>' + '<p>' + self._origin + '<p>' + '<p>' + self._story + '<p>' + '<p>' + self._locations + '<p>' + '<p>' + self._colors + self._div_end + self._footer
