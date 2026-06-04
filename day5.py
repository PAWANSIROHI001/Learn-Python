#  we are learn today type casting
# type casting is the process of converting one data type to another data type
# there are two types of type casting
# 1. implicit type casting
# 2. explicit type casting
# implicit type casting is done by the python interpreter automatically
# explicit type casting is done by the programmer using built-in functions

# implicit type casting

a = 10
b = 20.5
c = a + b
print(c)  # output: 30.5
print(type(c))  # output: <class 'float'>

# explicit type casting 

x = 10
y = 20.5
z = int(y)  # converting float to int
print(z)  # output: 20
print(type(z))  # output: <class 'int'>

#  note : we can add two multiple data types only sting and int or float and int but we cannot add string and int or string and float

# for example: 

a = "10"
b = 20
c = a + b  # this will give an error because we cannot add string and int
print(c)

