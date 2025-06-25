# dipslay all buildin exceptions and functions
print(dir(__builtins__))

#print(0)
print("python")

#len()
alist = [10,20,30]
print(len(alist))

book = {"chap1":10,"chap2":20,"chap3":30}
print(len(book))

#input()
name = input("Enter any name :")
print(name)

#max()
print(max(alist))
#min()
print(min(alist))
#sum()
print(sum(alist))

#id() - memmory reference of object
name = 'python'
print(id(name))
alist = [10,20,30]
print(id(alist))

# typecasting - converting from one object to another object
# str()   int()    list()   tuple()   set()    dict()   oct()  hex()

val = 1
valstr = str(val)    # number to string  # '1'
print(type(valstr))

alist = [10,20,30]
print(tuple(alist))   # list to tuple

atup = (40,50,50)
alist = list(atup)    # tuple to list

name = 'python'
output = list(name)
print(output)


alist = [10,20,30,30,30,30,30,30,20,20,20]
print(set(alist))


mydict = dict()
print("empty dictionary", mydict)

# create dictionary from list of tuples
pairs = [('a',1),('b',2),('c',3)]
print(dict(pairs))


data = dict(chap1=10,chap2=20,chap3=30)
print(data)

keys= ["chap1","chap2","chap3"]
values=[10,20,30]
data = dict(zip(keys,values))
print(data)

data = list(zip(keys,values))
print(data)


string1 = "ABC"
string2 = "123"
output = list(zip(string1,string2))
print(output)