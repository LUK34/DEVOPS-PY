def sumOfNumber(a=1,b=2,c=3):
    sum=a+b+c
    return sum

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print("Sum of numbers using default argument: ", sumOfNumber())
print("Sum of numbers NOT using default argument -> 1 argument -> using a= ",a," ,SUM=> ", sumOfNumber(a))
print("Sum of numbers NOT using default argument -> 1 argument -> using b= ",b," ,SUM=> ", sumOfNumber(b))
print("Sum of numbers NOT using default argument -> 1 argument -> using c= ",c," ,SUM=> ", sumOfNumber(c))
print("Sum of numbers NOT using default argument -> 2 arguments -> using a= ",a,", b= ",b," ,SUM=> ", sumOfNumber(a,b))
print("Sum of numbers NOT using default argument -> 2 arguments -> using a=",a,", c= ",c," ,SUM=> ", sumOfNumber(a,c))
print("Sum of numbers NOT using default argument -> 2 arguments -> using b=",b,", c= ",c," ,SUM=> ",sumOfNumber(b,c))
print("Sum of numbers NOT using default argument -> 3 arguments -> using a=",a,", b= ",b,", c= ",c, " ,SUM=> ", sumOfNumber(a,b,c))
