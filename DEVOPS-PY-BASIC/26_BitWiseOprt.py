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
print("Bitwise LEFT SHIFT -> << ")
# a<<n = a×2^n
# a is the number to be shifted.
# n is the number of positions to shift left.
# The result is a multiplied by 2^n
print("12 << 2 = ", 12 << 2)
print("0o21 << 3 = ", 0o21 << 3)
print("0x21 << 3 =", 0x21 << 3)
print("----------------------------------------------")
print("Bitwise RIGHT SHIFT -> >> ")
# a>>n= A/2^n
# a is the number to be shifted.
# n is the number of positions to shift right.
# The result is the integer division of a by  2 ^ n
print("12 >> 2 = ", 12 >> 2)
print("0o21 >> 3 = ", 0o21 >> 3)
print("0x21 >> 3 =", 0x21 >> 3)
print("----------------------------------------------")
print("Special Operator -> id ")
print("1. id()")
a7 = 121
b7 = 1.21
print("The id() function in Python is used to get the unique identity (memory address) of an object. "
      "This identity remains constant for an object during its lifetime.")
print("id(a7) = ",id(a7))
print("id(b7) = ",id(b7))
# 2 types of identity operators:
# 1) is
# 2) is not
# return boolean values as an output.

# is:
    # True -> when 2 objects address is same.
    # False -> when 2 objects address is different.
# is not:
    # True -> when 2 objects address is different.
    # False -> when 2 objects address is same.
a8=10
b8=20
c8=a8
print("Address of a8 = ", id(a8))
print("Address of b8 = ", id(b8))
print("Address of c8 = ", id(c8))

print("a8 is b8 = ", a8 is b8)
print("a8 is c8 = ", a8 is c8)

print("a8 is not b8 = ", a8 is not b8)
print("a8 is not c8 = ", a8 is not c8)
print("----------------------------------------------")
print("Membership Operator: ")
# to check whether the element is belonging to the collection/string or not.
# 2 membership operators:
# 1) in
# 2) not in
# these are also return boolean values

# in:
# True -> when the specified element is belonging to the main data
# False -> otherwise

# not in:
# opposite to in operator


