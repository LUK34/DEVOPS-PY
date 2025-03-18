# Write a python program to print all perfect numbers from 1 to 100
"""
Perfect number: Sum of all the factors of the given number excluding itself is equal to given number is called as "Perfect number"

ex: 48 ==> 1,2,3,4,6,8,12,16,24,48
1+2+3+4+6+8+12+16+24+48 ==>78
78 == 48 ==> is not a perfect number
"""

for i in range (1,501):
    s=0
    print("The factor for:", i)
    for j in range(1,i+1):
        if(i%j ==0):
            print(j,end="\t")
            s=s+j
    print()

























