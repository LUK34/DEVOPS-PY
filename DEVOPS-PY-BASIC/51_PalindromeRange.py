n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

for n in range(n1,n2+1): #100 to 1000
    m=n; #121
    reverse=0
    while m!=0:
        digits=m%10; # 1 , 2 , 1
        reverse=reverse*10+digits # 0+1 , 1*10 + 2 , 12*10 + 1
        m=m//10 #12,1
    if reverse == n: # 121 == 121
        print(n,end="\t")
