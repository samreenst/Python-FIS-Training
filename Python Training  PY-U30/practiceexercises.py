from datetime import datetime
a=datetime.now()
b= a.strftime('%d-%m-%y')
print(b)

#unpacking tuple

tuple = (1,2,3,4,5,6,78,8,)
a,*b,c = tuple
print(a)
print(b)
print(c)
