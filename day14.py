# today we learn tuple:
# tuple cannot be changed

# for example:

tuple= (1,2,3,4,5,6,7)
print(tuple)
print(type(tuple))

# methods of tuple

colour = ("red", "black", "green", "orange")
color = list(colour)
color.append("blue")
color.pop(3)
color[1] = "white"
colour = tuple(color)
print(colour)


# only can change tuple change into list