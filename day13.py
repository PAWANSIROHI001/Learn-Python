# python list

# list is changeable

# for example:

marks = [6,9,4,8,"sirohi",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

# this is the negative index

print(marks[-3])
print(marks[len(marks)-3])

# positive index

print(marks[5-2])
print(marks[2])


# to cheak the element in the list

if 6 in marks:
    print("sirohi")
else:
    print("no") 


# Range in list;

print(marks)
print(marks[1:4])
print(marks[1:-1])
print(marks[1:3:2])
