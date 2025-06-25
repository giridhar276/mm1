

aset = {10,10,10,20,20,20,30,30}
bset = {30,30,30,40,40,40,50,50}

aset.add(10)
print("After adding :", aset)
aset.add(100)
print("After adding :", aset)
print(aset)
print(bset)

print("Union :",aset.union(bset))
print("Intersection :", aset.intersection(bset))
print("Difference :", aset.difference(bset))
print("subset :",aset.issubset(bset))
print("superset:", aset.issuperset(bset))