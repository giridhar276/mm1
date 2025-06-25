
#fobj = open("C:\\new\\data.txt","w")
#fobj = open("C:/new/data.txt","w")
#fobj = open(r"C:\new\data.txt","w")  #  raw string
fobj = open("data.txt","w")

fobj.write("python\n")
fobj.write("unix\n")
fobj.writelines(["java","spark","pyspark"])


for val in range(1,10):
    fobj.write(str(val) + "\n")

fobj.close()


name = "python"
print(name.encode())
