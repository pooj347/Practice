y = int(input("enter the year to check:"))

# Check if the year is divisible by 4
if y % 4 == 0:
    
    # Check if the year is divisible by 100
    if y % 100 == 0:
        
        # Check if the year is divisible by 400
        if y % 400 == 0:
            
            # Divisible by 400, it is a leap year
            print("Leap year") 
        else:
            print("Not a leap year")  
    else:
        print("Leap year") 
else:
    print("Not a leap year")
