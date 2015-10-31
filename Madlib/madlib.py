'''
    Elimarie Morales Santiago
    Full Sail University
    MadLib
    Assignment in INTRODUCTION TO PYTHON
    Professor: Rebecca Carroll
'''

# I am not very good with stories but I tried to make it work

#this will store user input
dictionary = {}

#main game function
def madlib():
    #this will print the title welcome message
    print "Welcome to Elimaries MadLib game!"

    #this will ask user to input his name
    name = raw_input("Enter your Name:")

    #this will ask user to input BFF name
    relative = raw_input("What is your best friends name:")

    #this will ask the user to input is birth year
    years = int(raw_input("Enter your birth year:"))

    #this wil add hobbies to dictionary aray objects
    dictionary['hobbie1'] = raw_input("Enter your favorite hobby:")
    dictionary['hobbie2'] = raw_input("Enter your second hobby:")

    #this will ask the average distance from the user travel to work
    distance = float(raw_input("Which is your mile average distance commute to work:"))

    #this will ask user for hour number
    time = float(raw_input("How many hours have you been awake today?:"))

    #this story will start printing from here
    print name, "is", 2015 - years, "years old."
    print name, "and", relative, "need to do something today."








































