#python program to find selling price with given cost and discount

#cost price of product cp
cp= float(input("enter cost price: "))
#discount in percentage ds
ds= float(input("enter discount%:"))
#discount on cost price
discountamount=cp*ds/100
sp=cp-discountamount
print("cost price : ",cp)
print("discount: ",discountamount)
print("selling price : ",sp)
