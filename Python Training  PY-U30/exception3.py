from re import X


try:
    print(x)
except Exception as e:
    print("You have encountered an exception ",e)
else:
    Print("It is all good")
finally:
    print("It is finished")