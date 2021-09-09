def addloop(groceries):
    print(groceries)
    price = 0.00
    for x in groceries:
        #price = price + x #longway
        price += x
    return price



#MAIN
groceryprices = [12.12, 13.23, 6.00]
addloop(groceryprices)
print(addloop(groceryprices))
print(sum(groceryprices))