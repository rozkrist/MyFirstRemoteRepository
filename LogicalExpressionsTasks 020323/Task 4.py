year = int(input("Please enter a year:"))
leapyear = year%400==0 or (year%4==0 and year%100!=0)
print ("Leap year :" + str(leapyear))