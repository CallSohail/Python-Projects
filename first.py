# Unpack a Collection
fruits = ["Banana", "Apple", "Mango"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
line = "'International English Language Testing System'"
def myfun():
    line = "IELTS"
    print("Ielts stand for --> " + line)

myfun()
print(line)

# Random Number
import random
print(random.randrange(1, 10))

# Multiline string
multi_line = """My name is Muhammad Sohail and 
I am the student of computer science at the university of malakand
Today I wanna show you the basics of python."""
print(multi_line)

name = " Sohail "
# print(name[0])
for x in name:
    print(x)

# strip function: if you want to remove the spaces from the text you can used the strip function

print(name.strip())

# upper case
print(name.upper())

# Lower Case
print(name.lower())

#Replced a word
print(name.replace('o', 'u'))

# Split String
h1 = "Hello, Pakistan"
print(h1.split(','))

# The list() Constructor
thislist = list(("Salman", "Sohail", "Rehan"))
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)