'''
    Elimarie Morales Santiago
    Full Sail University
    MadLib
    Assignment in MadLibrary
    Professor: Rebecca Carroll
'''

# I am not very good with stories but I tried to make it work

#this will store user input
dictionary = {}

#this will store my suggestion
suggest = ["go back to your room", "and take a nap"]

#this will calculate time
def calculate(distance,time):
    return "Well you have been awake for the last %.0f(hours) %.0f(m) " \
           "now go get some sleep you only have %.0fm/h!" % \
           (distance, time, distance / time)

#main game function
def madlib():
    #this will print the title welcome message
    print "Welcome to Elimaries MadLib game!"

    #this will ask user to input his name
    name = raw_input("Enter your Name: ")

    #this will ask user to input BFF name
    relative = raw_input("What is your best friends name: ")

    #this will ask the user to input is birth year
    years = int(raw_input("Enter your birth year: "))

    #this wil add hobbies to dictionary aray objects
    dictionary['hobbie1'] = raw_input("Enter your favorite hobby: ")
    dictionary['hobbie2'] = raw_input("Enter your second hobby: ")

    #this will ask the average distance from the user travel to work
    distance = float(raw_input("Which is your mile average distance commute to work: "))

    #this will ask user for hour number
    time = float(raw_input("How many hours have you been awake today?: "))

    #this story will start printing from here
    print name, "is", 2015 - years, "years old."
    print name, "and", relative, "need to do something today."

    #this will check if it is your or old
    if years > 41:
        print "you guys are to old to", dictionary['hobbie2']
    elif years >= 15 or age == 21:
        print "you guys are to young to", dictionary['hobbie1']
    print "you guys should:"
    for string in suggest:
        print string
    print calculate(distance, time), "you should be tired tomorrow is another day"

madlib()


'''
GAME  TESTED

Welcome to Elimaries MadLib game!
Enter your Name:Eli
What is your best friends name:Mirelys
Enter your birth year:1975
Enter your favorite hobby:Drink
Enter your second hobby:Sleep
Which is your mile average distance commute to work:2.5
How many hours have you been awake today?:12
Eli is 40 years old.
Eli and Mirelys need to do something today.
you guys are to old to Drink
you guys should:
go back to your room
and take a nap
Well you have been awake for the last 2(hours) 12(m)
now go get some sleep you only have 0m/h! you should be tired tomorrow is another day
'''







































