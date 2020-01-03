#functions is collection of code create to complete specific task

def say_hi_to ():
    user = input("Hi, what's your name: ")
    print("Hello user, " + user)

say_hi_to()

def sayhi(name, age):
    print("Hello " + name + "Age: " + age)

sayhi("Milli", "345")

#RETURN STATEMENT

#This return statement inside of function return the information from function
#nothing below return statement in function will not work!
#return breaks the function

def  cube(number):
    return number*number*number

result = cube(4)
print(result)

