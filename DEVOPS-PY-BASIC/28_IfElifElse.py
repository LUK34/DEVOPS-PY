n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
n4=int(input("Enter the fourth number:"))

if(n1>n2 and n1>n3 and n1>n4):
    print("n1 is the biggest number.")
elif n2>n3 and n2>n4:
    print("n2 is the biggest number.")
elif n3>n4:
    print("n3 is the biggest number.")
else:
    print("n4 is the biggest number.")