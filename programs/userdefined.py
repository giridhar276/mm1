# fixed arguments
def display(a,b):
    print(a,b)
display(10,20)

# default arguments
def display(a = 0,b = 0,c = 0,d = 0):
    print(a,b,c,d)
display()
display(10)
display(10,20)
display(10,20,30)
display(10,20,30,40)

# keyword arguments
def display(c,b,a):
    print(a,b,c)
display(b=20,a=10,c=30)

#variable length arguments

def display(*args):
    for i in args:
        print(i)
display(10,20,30,40,50,60,70,80,90,100,56,43,5,4,5,3,5,43,4,56,3,45,3,644,23,5,43,4,3,35)