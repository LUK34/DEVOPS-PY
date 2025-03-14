n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
n4=int(input("Enter the fourth number:"))

if (n1<n2) and (n1<n3) and (n1<n4):
    print("n1= ",n1," is the smallest number.")
elif (n2<n3) and (n2<n4):
    print("n2= ", n2, " is the smallest number.")
elif (n3<n4):
    print("n3= ", n3, " is the smallest number.")
else:
    print("n4= ", n4, " is the smallest number.")