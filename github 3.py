Principle = float(input("enter Principle:"))
Rate = float(input("enter Rate:"))
Time = float(input("enter Time(n years):"))
Simple_interest = (Principle*Rate*Time)/100
Amount = Principle *(pow((1+Rate/100),Time))
Coumpound_interest = Amount-Principle
print("Simple interest:",Simple_interest)
print("Coumpound interest:",Coumpound_interest)
