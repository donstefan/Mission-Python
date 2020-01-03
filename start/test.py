from math import *

character_name = "Jasna"
character_age = "35"
phrase = "fuck this shit"
mod = 10 % 3
print("Hello world, " + character_name)
print(phrase + " for good")
print(len(phrase))
print(phrase[3])

print(phrase.index("shit"))

print(phrase.replace("shit", "life"))

print(str(mod) + " mu fav num")

print(pow(4, 2))
print(round(3.2))
print(max(3, 5, 7, 2))

print(sqrt(9))


#input from user

name = input("Please add your name: ")
age = input("Please add your age: ")
print("Hi, " + name + ". You are: " + age)