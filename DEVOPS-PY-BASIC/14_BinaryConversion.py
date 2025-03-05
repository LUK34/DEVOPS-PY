a=102   #Decimal
b=0o102 #Octal
c=0xaf12 #Hexadecimal
d=True
e=False

print("Decimal to Binary: " ,bin(a)) # Decimal to Binary -> Divide the number by 2 and whatever reminder you get -> 0 or 1 take that from bottom to top
print("Octal to Binary: " ,bin(b)) # Octal to Binary -> 001(1) 000(0) 010(2) (421 Rule)
print("Hexadecimal to Binary: " ,bin(c)) # Hexadecimal to Binary -> 1010(a) 1111(f) 0001(1) 0010(2) (8421 Rule)
print("Boolean to Binary: ", bin(d)) # Boolean to Binary -> 0b1
print("Boolean to Binary: ", bin(e)) # Boolean to Binary -> 0b0
print("For binary  conversion, we cannot use float, complex and strings")
# print(bin(1.5))
# print(bin(1+2j))
# print(bin('101'))