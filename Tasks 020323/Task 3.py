int1 = input("Please write one number:")
int2 = input("Please write second number:")
a = int(int1)
b = int(int2)
result = a%2==0 and b%2==0
print("Both numbers are even:" + str(result))

result = a%2==0 or b%2==0
print("At least one number is even:" + str(result))