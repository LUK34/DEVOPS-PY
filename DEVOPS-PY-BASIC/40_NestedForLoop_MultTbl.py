# Write a python program to print all multiplication tables from 1 to 10

for number in range(1,11):
    print("Table for:", number)
    for i in range(1,11):
        print(number,"X",i,"=", number*i)
    print()
    print("----------------------------------------")

# Write a python program to print all multiplication tables from 11 to 20
for number in range(11,21):
    print("Table for:", number)
    for i in range(1,11):
        print(number,"X",i,"=", number*i)
    print()
    print("----------------------------------------")
