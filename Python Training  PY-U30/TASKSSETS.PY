set1={'Lily','Daisy','Rose','Sunflower'}
set2={'Jasmine','Sunflower','Marigold'}

#print(set1.difference(set2))
#print(set2.difference(set1))

print(set1.remove('Sun'))
print(set1.discard('flower'))
print(set1.pop())
print(set1.clear())
del set1
print(set1)