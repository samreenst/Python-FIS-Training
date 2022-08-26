dict1={"Age" : 22, "Name" : "Samreen", "Dept" : ['cse','ece','it']}

for x in dict1:
    print(dict1[x])

for x in dict1.values():
    print(x)


for x in dict1.keys():
    print(x)

for x,y in dict1.items():
    print(x, ':' ,y)

print("Adding new items")
dict1["university"] = "anna"
print(x)

x = dict1.items()
print(x)


# modifying an item
dict1["Age"] = 23
print(dict1)

#popping an item
print(dict1.pop("Age"))

#removing an item from  a dictionary
print(dict1.remove("Age"))

print(dict1.clear())