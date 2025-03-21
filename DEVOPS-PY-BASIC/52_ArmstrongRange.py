n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

for i in range(n1,n2+1): #100 to 1000
    length=len(str(i))
    sumOfPower=0
    n=i #153
    while n!=0:
        digits=n%10 #3, 5, 1
        powers=digits**length #27, 125
        sumOfPower+=powers #27+0, 125 + 27, 152 + 1=153
        n=n//10 #15,1
    if sumOfPower == i: #153==153
        print(i,end="\t")