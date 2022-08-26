def Convert(list):
    dict = {list[i] : list[i+1] for i in range(0,len(list),2)}
    return dict

list = [1,'Samreen',3,'Dina',4,16]
print(Convert(list))