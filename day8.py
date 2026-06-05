# use of string slicing and operations 

names = "Sirohi,Alice, Bob, Charlie, David"
print(names)
len1 =(len(names))
print (len1)

# slicing the string to get the first name
name = names[0:6]
name = names[:]  #python automatically calculates the length of the string and slices it accordingly
print(name)


# slicing the string to get the second name
name = names[7:12]  
print(name)

