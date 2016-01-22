"""
# ELIMARIE MORALES SANTIAGO
# FULL SAIL UNIVERSITY
# Design Patterns for Web Programming - Online
# Reusable Library
"""
# Thi will insert or append methods to display in the correct html pages"""

from library import PetInfo

class Start(object):
    def __init__(self):
        self.title = "Pets Subscription"
        self.css = "styles.css"

    @property
    def show(self):
        return open("index.html").read().format(**locals())
         # Show content in html page """

class PetList(object):
    def __init__(self, pets):
        self.title = "Subscription Update"
        self.css = "styles.css"
        self.pets = pets
        self.pet_show = PetInfo(pets).pet_show()
        # Get class for an html data of pet """

    @property
    def show(self):
        return open("pet_list.html").read().format(**locals())
         # Show content in html page """