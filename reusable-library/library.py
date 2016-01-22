"""
# ELIMARIE MORALES SANTIAGO
# FULL SAIL UNIVERSITY
# Design Patterns for Web Programming - Online
# Reusable Library
"""

# Class holding the attributes """
class Pet(object):
    def __init__(self):
        self.__name = None
        self.__breed = None
        self.__age = None
        self.__gender = None
        self.__category = None
        self.__email = None

# getters """

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def category(self):
        return self.__category

    @property
    def email(self):
        return self.__email

# setters """

    @name.setter
    def name(self, user_input):
        self.__name = user_input

    @breed.setter
    def breed(self, user_input):
        self.__breed = user_input

    @age.setter
    def age(self, user_input):
        self.__age = user_input

    @gender.setter
    def gender(self, user_input):
        self.__gender = user_input

    @category.setter
    def category(self, user_input):
        self.__category = user_input

    @email.setter
    def email(self, user_input):
        self.__email = user_input

class PetInfo(object):
    def __init__(self, pets):
        self.__pets = pets

    def new_pet(self, pet):
        self.__pets.append(pet)

 # This will store, attach, and show the information on pet_list.html """

    def pet_show(self):

        pet_list = " "
        # This will generate table with pet info """
        for pet in self.__pets:
            pet_list += "<tr>"
            pet_list += "<td>%s</td>" % pet.name
            pet_list += "<td>%s</td>" % pet.breed
            pet_list += "<td>%s</td>" % pet.age
            # if pet age is grater than 2 the pet will compete """
            if int(pet.age) >= 2:
                pet_list += "Your Pet is Ready for Competition!"
            # elif pet age is less than 1 the pet can't compete """
            elif int(pet.age) <= 1:
                pet_list += "Sorry your pet is to young, Try again Next Year."
            pet_list += "<td>%s</td>" % pet.gender
            pet_list += "<td>%s</td>" % pet.category
            pet_list += "<td>%s</td>" % pet.email
            pet_list += "</tr>"

        return pet_list
