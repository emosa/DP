"""
# ELIMARIE MORALES SANTIAGO
# FULL SAIL UNIVERSITY
# Design Patterns for Web Programming - Online
# Reusable Library
"""

import webapp2  # used the webapp2 library """
from page import *  # * will import all classes from the page """
from library import *  # * will import all classes from the library """

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # array that hold pet info """
        pets = []

        if self.request.GET: # Check if GET exists """
            # Get form data from user input """
            contest_pet = Pet()
            contest_pet.name = self.request.GET["name"]
            contest_pet.breed = self.request.GET["breed"]
            contest_pet.age = self.request.GET["age"]
            contest_pet.gender = self.request.GET["gender"]
            contest_pet.category = self.request.GET["category"]
            contest_pet.email = self.request.GET["email"]
            pets.append(contest_pet)
            # Create the occurrence of pet list page """
            pets_page = PetList(pets)
            # Write response to page """
            self.response.write(pets_page.show)
        else:
             # Create occurrence and write response to page """

            self.response.write(Start().show)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
