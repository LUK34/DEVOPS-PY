def typeOfTriangle(a,b,c):
    print("Value of a= ",a,"Value of b= ",b,"Value of c= ",c)
    if a==b and a==c:
        print("It is an Equalateral Triangle.")
    elif a==b or a==c or b==c:
        print("It is an Isosceles Triangle.")
    else:
        print("It is Scalene Triangle.")

print("----------------------------------------------------------")
p=int(input("Enter the first side of the triangle:"))
q=int(input("Enter the second side of the triangle:"))
r=int(input("Enter the third side of the triangle:"))
print("Value of p= ",p,"Value of q= ",q,"Value of r= ",r)
typeOfTriangle(c = r, a = p, b = q)
print("----------------------------------------------------------")