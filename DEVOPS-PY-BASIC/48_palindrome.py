

number=int(input("Enter a value:")) #9876

reverse=0
n=number
while n!=0:
    remainder=n%10 # Modulous -> 6 7 8 9
    reverse=reverse*10+remainder # 6 67 6789
    n= n//10 # Floor Division -> 987 98 9 8
print("------------------------------------------------")
print("The FINAL VALUE after reverse = ",reverse)
if(number == reverse):
    print("The number: ", number," and reverse: ",reverse," are PALINDROME")
else:
    print("The number: ", number, " and reverse: ", reverse, " are NOT PALINDROME")