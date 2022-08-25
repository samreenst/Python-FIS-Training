"""
a = [1,'Samreen',3,5,38298928]
for i in a:
    print(i)
print(a)
for x in range(len(a)):
    print("At index : ", x," --->",a[x])
"""
grades=[90,88,97,88,80,98]
grades.append(99)
print(grades)
a=[1,2,3,4,5]
b=[6,7,8]
a.extend(b)
print(a)
c=a+b
print(a)
print(grades.count(88))
grades[2]=99
print(grades)
grades.remove(88)
print(grades)
print(grades.pop(1))
print(grades.index(90))