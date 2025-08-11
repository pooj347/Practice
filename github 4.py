cp= float(input("enter the cost price of the product:"))
sp= float(input("enter the selling price of the product:"))

if cp==sp:
    print("No profit No loss")
else:
 if sp>cp:
     print("profit of the product is:",sp-cp)
 else:
  print("loss of the product is:",cp-sp)
