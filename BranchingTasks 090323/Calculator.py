number1, number2 = input("Please enter any two numbers:").split() 
operation = input("Please select the operation to perform: *,/,+,- or %:")
int1 = int(number1)
int2 = int(number2)
while operation !="+" and operation!="-" and operation!="*" and operation!="/" and operation!="%":
    operation = input("Operation provided isn't valid, please try again:")
else:
    if operation == "+":
        result = int1+int2
    elif operation =="-":
        result=int1-int2
    elif operation =="*":
        result=int1*int2
    elif operation =="/":
        result=int1/int2
    elif operation =="%":
        result=int1%int2
    print(result)  
