# Write a python program to reverse the given number:

number=int(input("Enter a value:")) #9876

reverse=0
n=number
while n!=0:
    print("The value of n after floor division: ", n)
    remainder=n%10 # Modulous -> 6 7 8 9
    print("The value of remainder after modulous: ", remainder)
    reverse=reverse*10+remainder # 6 67 6789
    print("The value of reverse: ", reverse)
    n= n//10 # Floor Division -> 987 98 9 8
print("------------------------------------------------")
print("The FINAL VALUE after reverse = ",reverse)



