try:
    a=100/0
except  ZeroDivisionError:
    print("You are dividing by zero")
else:
    print(a)
finally:
    print("Exception is handled!")
