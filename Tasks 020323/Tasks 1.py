age = int(input ("Please enter your age:"))
driverslicense = input ("Do you have a driver's license:")
result = age>=18 and driverslicense == "yes"
print ("You are able to drive:" + str(result))
