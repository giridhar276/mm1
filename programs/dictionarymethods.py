
book = {"chap1":10 ,"chap2":20 ,"chap3":30}
print(book)
# add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)
# print individual value
print(book["chap1"])
print(book["chap2"])
# dissplay keys
print(book.keys())
# display values
print(book.values())
# display itms
print(book.items())

book.pop("chap1") #chap1-10 will be removed from dict
print(book)

book.popitem()  # will remove last inserted key value
book.popitem()
print(book)

# combining two dictionaries
newbook= {"chap7":70 ,"chap8":80}
print(newbook)
finalbook = {**book, **newbook}
print(finalbook)

book.update(newbook)
print("updated book:", book)

# display keys
for key in book.keys():
    print(key)

# display values
for value in book.values():
    print(value)

for k,v in book.items():
    print(k,v)