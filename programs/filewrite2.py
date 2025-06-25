
# traditional way
fobj = open("data.txt","w")
fobj.write("python\n")
fobj.close()



# pythonic way
# context manager
# If any line starts with keyword with ... it is called context manager
# Advantage :  file gets closed automatially  when it comes out of indentation
filename = input("Enter any filename :")
with open(filename,"w") as fobj:
    fobj.write("python\n")
    fobj.writelines(["abc","def"])
    print(fobj.closed)

print(fobj.closed)



