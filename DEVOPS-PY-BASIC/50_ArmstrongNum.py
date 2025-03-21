# To check if the given number is armstrong or not.

number=int(input("Enter a value:")) #153 is an armstrong number
leny=len(str(number))
n=number
sumOfDigits=0
while n !=0:
    individualDigits=n%10 #3 5 1
    sumOfDigits=sumOfDigits + (individualDigits**leny) # 0+ 3^3,  27+5^3, 152+1^3
    n = n // 10 #15 1
if(sumOfDigits == number):
    print("The number entered = ",number," is an armstrong number")
else:
    print("The number entered = ", number, " is NOT an armstrong number")

# 1+125+27=152+1=153

