"""
try:
    age =18
    if age<18:
        raise ValueError(age)
except:
    print("You cannot vote")
else:
    print("You can vote")
    """
try:
    age = 18
    if age<18:
        raise ValueError(age)
except:
    print("You cannot vote")