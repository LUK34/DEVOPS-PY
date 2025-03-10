print("----------------------------------------------")
print("Bit Wise AND operation: &")
print("10 & 20", 10 & 20) #1010 & 10100
print("0o12 & 0x12",0o12 & 0x12)
print("----------------------------------------------")
print("Bit Wise OR operation: |")
print("10 | 20", 10 | 20) #1010 | 10100
print("0o12 | 0x12",0o12 | 0x12) #00001010 | 00010010
print("----------------------------------------------")
print("Bit Wise XOR operation: ^")
# a=0 , b=0 , a^b=0
# a=0 , b=1 , a^b=1
# a=1 , b=0 , a^b=1
# a=1 , b=1 , a^b=0
print("10 ^ 20",10 ^ 20)
print("----------------------------------------------")
# print(1.2 & 2.3)      #Type Error
# print (1.2 | 2.3)     #Type Error
# print (1.2 ^ 2.3)     #Type Error
# print(1+2j & 2-3j)    #Type Error
# print('a' | 'b')    #Unsupported operand type

# True ->  1 -> 0001
# False -> 0 -> 0000
print(True & True)
print(True | False)
print(True ^ False)
print("----------------------------------------------")
print("Bitwise NOT -> ~")
print("~0", ~0)
print("~1", ~1)
print("~-1", ~-1)
print("----------------------------------------------")






