def display(a,b):
    c = a + b
    return c
total = display(10,20)
print(total)

# lambda function
# lambda is the replacement of single liner function
# syntax
#functioname = lambda variables : expression
display = lambda a,b : a + b
total = display(10,20)
print(total)

length = lambda s : len(s)
print(length("python"))

upper = lambda s: s.upper()
print(upper("hello"))

upper = lambda s: s.upper()
print(upper("hello"))

maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # 20

age_check = lambda age: "Adult" if age >= 18 else "Minor"
print(age_check(17))  # Minor

result = lambda marks : "pass" if marks >=35 else "Faail"
print(result(30))


result = lambda marks : 'A' if marks >=90 else 'B' if marks>=75 else 'C'
print(result(80))


alist = [10,20,30,40]
blist = []
#output: [15,25,35,45]
for val in alist:
    blist.append(val + 5)
print(blist)

#map(function,iterable)
alist = [10,20,30,40]
print(list(map(lambda x:x+5 , alist)))   #[15,25,35,45]



floats = [2.5, 3.6, 4.1]
ints = list(map(lambda x: int(x), floats))
print(ints)



names = ["alice", "bob", "carol"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names) 



names = ["alice", "bob", "carol"]       #[5,3,5]
upper_names = list(map(lambda x: len(x), names))
print(upper_names) 


data = {"a":1,"b":2,"c":3}

newdata = dict(map(lambda item : (item[0].upper(), item[1]) ,data.items()) )
print(newdata)


# dict(map(function,iterable))
# dict(map(lambdafnction, data.items()))
#dict(map(lambdafnction,[('a',1),('b',2)]))