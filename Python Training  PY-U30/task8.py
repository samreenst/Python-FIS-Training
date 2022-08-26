

stock = {"apples" :20, "orange" :10, "pears" :5}
rates = {"apples" :70, "orange" :40.5, "pears" :55, "banana" :10}
order = {"apples" :3, "orange" :7, "pears" :6, "pineapple" :2}

cost = {}
net_cost =1
for i in order:
    if i in stock:
        if order[i]<stock[i]:
            stock[i]=stock[i]-order[i]
            net_cost=stock[i]*order[i]
            cost[i] = net_cost
            print(cost)
        else:
            print("Item is available in stock")   
    else:
        print("not available")

print(cost)
