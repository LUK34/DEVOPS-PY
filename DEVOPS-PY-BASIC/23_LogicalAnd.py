# logical AND operator
print("---------------------------------------------")
print("With BOOLEAN Values: ")
print("True and True -> ",True and True)
print("True and False -> ",True and False)
print("False and True -> ",False and True)
print("False and False -> ",False and False)
print("---------------------------------------------")
print("With INTEGER Values: ")
print("0 and 0 -> ", 0 and 0)
print("0 and 1 -> ", 0 and 1)
print("1 and 0 -> ", 1 and 0)
print("1 and 1 -> ", 1 and 1)
print("---------------------------------------------")
print("With FLOAT Values: ")
print("1.23 and 0.00 -> ", 1.23 and 0.00)
print("0.0001 and 0.0101010 -> ", 0.0001 and 0.0101010)
print("0.0000000001 and 0.0000000101010 -> ", 0.0000000001 and 0.0000000101010)
print("---------------------------------------------")
print("With COMPLEX numbers: ")
print("1+0j and 0-1j -> ", 1+0j and 0-1j) # 1 and 0 -> 0
print("0j and 1-1j -> ", 0j and 1-1j) # 0 and 1 -> 0
print("---------------------------------------------")
print("With STRING: ")
print('a' and 'b')
print('  ' and 'r')
print('' and 'p')