# Write a python programme to find the sum of individual digits of a given number


number=int(input("Enter a value:")) #9876
sumOfDigits=0
n=number #9876
while n !=0:
    individualDigits=n%10
    sumOfDigits=sumOfDigits + individualDigits
    n=n//10
print("The sum of digits for number entered: ",number," is: ",sumOfDigits)

