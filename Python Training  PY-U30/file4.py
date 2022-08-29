f = open('text.txt','r')
g = open('textche.txt','a')

counter = 0
line =f.readline()
while line:
    counter=counter+1
    if(line[29:39]=='Chennai'):
        print("Chennai Record")
        print("Red number",counter)
        g.write(line)
        print(line)
    line = f.readline()
f.close()
g.close()