f = open('text.txt','r')
line = f.readline()
counter = 0
c=0.0
while line:
    counter=counter+1
    print('Record num  : ',counter)
    a =line[0:4]
    print('id          : ',a)
    b =line[5:15]
    print('Name        : ',b)
    c =line[17:27]
    print('Salary      : ',c)
    d =line[29:39]
    print('Place       : ',d)
    e =line[43:53]
    print('Email id    :' ,e)

    if d == 'Chennai':
       c = 110/100*int(c)
    elif d == 'Kolkata':
        c = 150/100*int(c)
    else:
         c= 200/100*int(c)
    print("New Salary   :",c)
    
    line = f.readline()
    print("*****************************************")

print("**********all records are processed***********")
print("Total number of records =",counter) 
list1 = [c,c,c,c,c,c,c,c,c,c,c,c]
print(max(list1))
print("**********************************************")
f.close()