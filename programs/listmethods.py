

alist = [10,45,56,32,67,3,82,49]

alist.append(90)
print("After appending:",alist)
alist.extend([93,18,61])
print("After extending:",alist)
alist.insert(0,100)   #list.insert(index,value)
print("After inserting:",alist)
alist.pop(3)  #list.pop(index)  # you are suppposed to pass index
print("After pop operation :",alist)
alist.remove(82)  # list.remove(value)
print("After removing :",alist)
alist.reverse()
print("After reversing:",alist)
alist.sort()
print("After sorting :",alist)
alist.sort(reverse=True)
print("After sorting :",alist)


if 49 in alist:
    alist.remove(49)
else:
    print("value not found")