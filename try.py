# print('Hello World')
# print('*'*11)
# x = 1

# students_count = 1000
# rating = 4.56
# is_published = True
# name = "Bhaumik Yadav"

# print(type(students_count))
# print(type(rating))
# print(type(is_published))
# print(type(name))

# course = "Python Programming"
# print(len(course))
# print(course[0], course[-1])
# print(course[0:3])
# print(course[:3])
# print(course[3:])

# print("LOL \"Escape \\Character")

# first = "Bhaumik"
# last = "Yadav"
# full = f'{first} {last}'
# print(full)

# course = "   Python programming   "

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.lstrip())
# print(course.rstrip())
# print(course.find("pro"))
# print(course.replace("o", "i"))
# print("pro" in course)
# print("swift" not in course)

# a = 1 + 3j

# print(type(a))

# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)
# print(10+3)

# import math 

# print(round(2.9))
# print(abs(-2.9))
# print(math.ceil(2.9))

# temp = 35

# if temp > 30:
#     print("Hot")
# else:
#     print("Not hot")

# message = "Hot" if temp > 30 else "Not Hot"

# print(message)

# high_income = False
# good_credit = True
# student = True

# if high_income and good_credit:
#     print('Eligible')
# elif good_credit and student:
#     print("Eligible")
# else:
#     print("Ineligible")


# # RULE - Age should be bw 18 and 65

# age = 22
# if age >=18 and age < 65:
#     print('Eligible')
# if 18 <= age < 65:
#     print('Eligible') # Cleaner code


# # Strings compare on unicode values 

# if "bag" > "apple":
#     print('Yes1')
# if "bag" > "bah":
#     print('Yes2')
# if "bag" > "Bag":
#     print('Yes3')
# if "bag" > "bags":
#     print('Yes4')

# #Loops

# for number in range(3):
#     print("Sending Message, Attempt:", number + 1, "Index:", number)

# for i in range(1, 10, 2):
#     print(i)


# # break statement, else with for loop

# successful = False

# for number in range(1, 4):
#     print("Attempt:", number)
#     if successful:
#         print('Successful')
#         break
# else:
#     print("Attempted 3 times and failed")


# # Nested Loops

# for i in range(1, 5):
#     for j in range(i, 5):
#         print(f"({i}, {j})")


# # Iterables

# print(type(5))
# print(type(range(5))) #iterable complex data type

# for x in "Python":
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)


# # While Loops

# i = 0

# while i < 5:
#     print(i)
#     i+=1

# command = ""

# while command.lower() != "exit":
#     command = str(input(">"))
#     print("ECHO", command)

# #Alt for above loop
# while True:
#     command = str(input('>'))
#     print("ECHO", command)
#     if command.lower() in ["exit", "esc"]:
#         break


# # Program to display even numbers bw 1, 10 using % instead of step in range method

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)


# # UDF - User Defined Functions

# import datetime

# def greet():
#     a = int(datetime.datetime.now().strftime("%H"))
#     if 5 <= a < 12:
#         print("Good Morning")
#     elif 12 <= a < 16:
#         print("Good Afternoon")
#     elif 16 <= a < 20:
#         print("Good Evening")
#     else:
#         print("Good Night")


# greet()


# # Arguments in functions

# def laugh(is_happy = True): # These are the parameters of a function
#     return "LOL" if is_happy else "Pokerface"

# print(laugh(False)) # The values which we provide for respected parameters are the arguments


# 2 Types of functions 
# 1 - Perform a task
# 2 - Return a value

# # * args variable number of arguments

# def mul(*args):
#     out = 1
#     for i in args:
#         out *= i
#     return out

# print(mul(2, 3))
# print(mul(2, 3, 4, 5, 6))

# # sort elements on the basis of xth index in a nested list

# a = [[1,2,3], [2,3,4], [1,2,3], [4,1,6]]
# x = 2

# out = sorted(a, key= lambda a:a[x])
# print(out)

