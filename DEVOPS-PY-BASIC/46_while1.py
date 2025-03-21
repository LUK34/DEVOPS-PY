# Write a python program to count the number of digits of the given number:
# Solution 1: using str()
number=int(input("Enter a number to calculate number of digits present:"))
print("Solution 1: using str() method:")
print("The number of digits of a number:", number, "is = ", len(str(number)))
print("Solution 2: using while loop and floor division of 10")
n=number
count=0
while n!=0:
    n=n//10 #floor division
    count=count+1
print("The number of digits in a number:",number, "is = ", count)