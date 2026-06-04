# today we learn taking input from the user
# we can take input from the user using the input() function
# the input() function takes a string as an argument and returns a string


# for example:

name = input("Enter your name: ")
print("Hello, " + name + "!")  # output: Hello Sirohi!

# another example:

a = input("Enter a number: ")
b = input("Enter another number: ")
print(a + b)

# the above code will give an error because we cannot add two strings
# we need to convert the strings to integers or floats before adding them

print(int(a) + int(b))  # output: 30


# that's all for today, see you tomorrow!
