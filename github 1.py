total=int(input("enter the maximum marks of a subject : "))

sub1=int(input("enter marks of the first subject : "))

sub2=int(input("enter marks of second subject : "))

sub3=int(input("enter marks of third subject : "))

sub4=int(input("enter marks of fourth subject : "))

sub5=int(input("enter marks of fifth subject : "))

average=(sub1+sub2+sub3+sub4+sub5)/5
print("average is  ",average)
percentage=(average/total)*100
print("according to the percentage, ")
if percentage >= 90:
    print("Grade:A")
elif percentage >= 80 and percentage < 90:
    print ("Grade:B")
elif percentage >= 70 and percentage <80:
    print("Grade:C")
elif percentage >=60 and percentage <70:
    print("Grade:D")
else:
    print("Grade:E")
