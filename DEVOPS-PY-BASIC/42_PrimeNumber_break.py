# Generate the range of numbers to check which are prime numbers
n1=int(input("Enter the first value of the range:"))
n2=int(input("Enter the second value of the range:"))
for i in range(n1,n2+1):
    flag=False
    for prime in range(2,i):
        if i%prime ==0:
            flag=True
            break
    if flag == False:
        print(i,end="\t")
