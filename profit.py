cp = float(input("Enter the Cost Price of the Product: "))
sp = float(input("Enter the Selling Price of the Prodcut: "))

if(sp>cp):
    profit = sp - cp
    print("Recieved profit: " , profit)
else:
    loss = cp - sp
    print("Recieved profit: " , loss)