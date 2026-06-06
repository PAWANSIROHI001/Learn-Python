# today we are dicussing (if, else and elif) statements in python.

# this is a simple program to check if a person is eligible to vote or not based on their age.

a = int(input("Enter a your age: "))
print("Your age is: ", a)

if a >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# second is if-else ststement

fruit = 300
budget = 200

if fruit <= budget:
    print("You can buy the fruit.") 
else:    
    print("You cannot buy the fruit.")

# now we will discuss about elif statement


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("You got A grade.")
elif marks >= 80:
    print("You got B grade.")
elif marks >= 70:
    print("You got C grade.")
elif marks >= 60:
    print("You got D grade.")
else:
    print("You got F grade.")

    print("Yah!")




