integer=int(input("Please enter a number: "))
if integer <=1:
    print("This number is not a prime number.")
else: 
    for i in range(2,integer):
        if integer%i==0:
            result = False
            break
        else:
            result=True
            continue
    if result == False:
        print ("This number is not a prime number.")
    else:
        print ("This number is a prime number.")