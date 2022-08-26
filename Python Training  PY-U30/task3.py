list1=[1,'Samreen',2,'Fathima',3,'Dina']

list2=[4,'Kavi',5,'Lisa',6,'Sandy']
list1.extend(list2)
print(list1)

dict1 = {list1[i] : list1[i+1] for i in range(0,len(list1),2)}

print(dict1)