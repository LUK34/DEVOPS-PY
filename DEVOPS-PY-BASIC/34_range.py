a=range(10)
print("----------------------------------------------------------------")
print(a)
print("list(a) => ",list(a))
print("list(range(20)) => ",list(range(20)))
print("range(start,stop,step) => ",list(range(10,100,10)))
print("----------------------------------------------------------------")
for i in range(10):
    print("Hi")
print("----------------------------------------------------------------")
n = int(input("Enter length of natural number series:"))
for i in range(1,n+1):
        print(i)
print("\n")
print("----------------------------------------------------------------")
for i in range(1, n+1):
    print(i,end=" -> ")
print("\n")
print("----------------------------------------------------------------")
for i in range(1, n+1):
    print(i,end="\t")
print("\n")
print("----------------------------------------------------------------")
n=int(input("Enter the length of the natural number series: "))
result=(n*(n+1))//2
print("The sum of ",n," natural number is = ", result)
print("----------------------------------------------------------------")
s=0
for i in range(1,n+1):
    s=s+i
print("The sum of ",n," natural number is = ",s)

