set1={3,1,2,'timmy','TOMMY',True}
print(set1)
#print(set1[2])
for x in set1:
    print(x)
#adding items in sets
print('Samreen' in set1)
set1.add('jerry')
print(set1)
set2={'Fathima',23,9.0}

#combining sets
set1.update(set2)
print(set1)
set1.union(set2)
print(set1)