grades = [66,98,87,0,56,77,90]
i=0
for i in range(len(grades)):
    assert grades[i]!=0, "This person has failed"
    if(grades[i] >=50):
        print("This person has passed")
    else:
        print("Needs improvement")
print("It is over")