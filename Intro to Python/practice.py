# line comment -solo un comentario
'''
Doc strings
Multiples comentarios
http:legacy.pythong.org//pep-0008/
'''
'''
first_name = "Kermit"
last_name = "De Frog"

print first_name

#response = raw_input("Enter your name   ")

#print response

#print "Hello there, ", response
'''
'''simple math
birth_year = 1975
current_year = 2015

age = current_year - birth_year
'''
# print age

'''
comments, variables and printing in python
assignment operators increment decrement suma resta


print "You are " +  str(age) + " years old"
'''
'''conditional and collections'''

# example 1
'''

budget = 7

if budget > 100:
    brand = 'Nike'
    print 'Yay! we can buy cool ' + brand + ' shoes'
elif budget > 70:
    print "We can at least get some Adidas"
else:
    print 'No cool shoes for me'
'''
# example 2
'''
budget = 7

if budget > 100:
    brand = 'Nike'
    #print 'Yay! we can buy cool ' + brand + ' shoes'
elif budget > 70:
    #print "We can at least get some Adidas"
    pass
else:
    pass   #means move on to the next line fill in later

characters =['Eli','Joel','Spoky', 'Tini']
characters.append("Obi")
#print characters
#print characters[0]

#Dictionary and arrays

movies = dict() #creates dictionary object

movies = {"Star Wars": "Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}

print movies ["Star Wars"]
'''
# i love loops!

# WHILE LOOP---------
'''
i = 0
while i < 9:
    print"The count is", i
    i = i+1

# print from 0 to 8
# FOR LOOP---------- count between set of numbers

for i in range(0, 11):
    print"The count is", i
    i += 1

# print from 0 to 9

'''

#"FOR EACH" LOOP ------- cycle through
'''

rappers = ["Tupac","Nas", "Biggie Smalls"]
for r in rappers:
   # print r
     #print "One of the best rappers is " + r
     pass

# FUNCTIONS --- def

def calcArea(h,w):
    area = h * w
   # print area
    return area

#calcArea(20,40);

a = calcArea(20, 40);
#print a

print "My area is " + str(a) + "sqft"
'''

# FUNCTIONS --- def with variable
'''
x = 2

def calcArea(h, w):
    area = h * w
    return area + x

#calcArea(20,40);

a = calcArea(20, 40);

print a

'''

'''put variables into larger strings '''
'''
weight = 200
height = 63
message = '''
#Your height is {height} and your weight is {weight}
'''
message = message.format(**locals()) #locals methods
print message
'''

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
message = message.format(**locals()) #locals methods
print message













































