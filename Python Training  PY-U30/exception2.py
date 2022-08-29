a=10/0
print(a)

try:
    b = 10/0
except a as e:#when you dont know the name of the exception
    print(e)
else:
    print(a)
