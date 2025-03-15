n=int(input("Enter the range:"))
print("The even natural number based on the range: ",n," is as follows: ")
for i in range(1,n+1):
    if(i%2!=0):
        print(i, end="\t")

# 24 +16+9