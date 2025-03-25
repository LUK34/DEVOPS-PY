def typeOfTriangle(a,b,c):
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
typeOfTriangle(r,p,q)
print("----------------------------------------------------------")