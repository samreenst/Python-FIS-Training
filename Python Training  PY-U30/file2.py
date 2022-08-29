f = open('text.txt','r')
line = f.readline()
counter = 0
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
    
    line = f.readline()
    print("*****************************************")

print("**********all records are processed***********")
print("Total number of records =",counter) 
print("**********************************************")
f.close()