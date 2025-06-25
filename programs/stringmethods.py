# p   y    t    h     o   n        p    r    o    g   r   a   m   m   i   n   g
# 0   1    2    3     4   5   6    7    8    9
# -18                                                           -5  -4   -3   -2  -1
name = "python programming"
# slicing
#string[start:stop:step]
print(name[0])
print(name[0:4])
print(name[0:4:2])
print(name[::])
print(name[:])
print(name[::3]) #ph
print("output:",name[-23:])
print(name[::-1])


print(name[::])
print(name[0:18:1])
print(name[::-1])

name = "python programming"
print(name.capitalize())
print(name.title())
print(name.replace("python","ruby"))
print(name.split(" "))
print(name.count("p"))
print(name.count("q"))
print(name.endswith("g"))
print(name.endswith("q"))
print(name.startswith("p"))
print(name.startswith("a"))
print(name.find("min"))  # if substring if returns the starting index of it.
print(name.find("abc"))  # if not found.. it returns -1
print(name.isalpha())
print(name.isalnum())
print(name.isupper())
print(name.islower())
aname = "  python "
print(len(aname))
print(len(aname.strip())) # remove whitespaces at both ends
print(len(aname.lstrip()))
print(len(aname.rstrip()))
name = "I love {} and {}"  # template
print(name.format("python","java"))
print(name.format("hyderabad","Bangalore"))

str1 = "python"
str2 = "programming"
finalstring = str1 + " " + str2
print(finalstring)

name = "python"
print(name.encode("utf-32"))


# if condition
if 1 < 2:
    print("true")

if name.isupper():
    print("string is upper")

if name.startswith("p"):
    print("its python")

# if-else
if name.isupper():
    print("string is upper")
    print("inside if")
    print("still inside if")
else:
    print("string is lower")

# if-elif-eif-elif-elif-else
lang  = input("Enter any langauge :")
if lang == "python":
    print("its python")
elif lang == "unix":
    print("its unix")
elif lang == "java":
    print("its java")
else:
    print("its someother language")


# for loop  # range(start,stop,step)
for i in range(1,11):
    print(i)


name = "python"
for char in name:
    print(char)

for i in range(10,1,-1):
    print(i)

alist = [10,20,30]
for val in range(0,len(alist)): # range(0,3)
    print(alist[val])  