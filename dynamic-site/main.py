"""
# ELIMARIE MORALES SANTIAGO
# FULL SAIL UNIVERSITY
# Design Patterns for Web Programming - Online
# Dynamic Site
"""

import webapp2  # used the webapp2 library """

from page import GemstonePage  # * will import all classes from the GemstonePage """
from data import *  # * will import all classes from the data """


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #  Creates an instance of the imported class page
        page = GemstonePage()
        gem = Gemstone()
        data = GemstoneInfo()

        if self.request.GET:  # Check if GET exists in url data""
            # Check for name that will be used to determine what will be displayed on page
            name = self.request.GET["name"]
            # name will set Gemstone() equal to the object in GemstoneInfo()
            if name == 'opal':
                gem = data.list[0]
            elif name == 'amethyst':
                gem = data.list[1]
            elif name == 'diamond':
                gem = data.list[2]
            elif name == 'topaz':
                gem = data.list[3]
            elif name == 'tourmaline':
                gem = data.list[4]
        # else it will default to the first object in GemstoneInfo()
        else:
            gem = data.list[0]

        # set html elements in page py equal to data py
        page._name = gem.name
        page._img = gem.img
        page._bio = gem.bio
        page._origin = gem.origin
        page._story = gem.story
        page._locations = gem.locations
        page._colors = gem.colors

        # print content in html page """
        self.response.write(page.print_out)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
