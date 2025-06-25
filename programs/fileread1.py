#method1
# fobj acts like an handler or pointer for nagivating
with open("data.txt","r") as fobj:
    for line in fobj:
        line = line.strip()
        print(line)

#method2   fobj.readlines ----------> list
with open("data.txt","r") as fobj:
    print(fobj.readlines())

#method3 fobj.read()  ------> single string
# not suggested for larger files
with open("data.txt","r") as fobj:
    print(fobj.read())

# method4 - using csv library
import csv
with open("data.txt","r") as fobj:
    reader = csv.reader(fobj) # converting file object to csv object
    for line in reader:
        print(line)

#method5 using pandas 
import pandas
df = pandas.read_csv("data.txt",header=None)
print(df)