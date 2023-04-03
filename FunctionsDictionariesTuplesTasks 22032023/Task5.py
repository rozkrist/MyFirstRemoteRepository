# Write a function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum.

def find_pair(integers,target_sum):
     seen = set()
     for number in integers:
         diff = target_sum - number
         if diff in seen:
             return [diff,number]
         # else:
         seen.add(number)
     return []

numbers = [4,8,19,5,3]
target_sum = 22
print(find_pair(numbers,target_sum))

