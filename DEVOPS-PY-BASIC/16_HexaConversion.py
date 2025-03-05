a=0b01010101
b=102
c=0o102

print("Binary to Hexadecimal",hex(a))
#01010101 -> Binary to Decimal
# Binary to Decimal -> 0*2^7+1*2^6+0*2^5+ 1*2^4 + 0*2^3 + 1*2^2 + 0*2^1 + 1 *2^0 =85
# Decimal to Hexadecimal -> 85 keep dividing this number by 16, take the reminder from bottom to top.

print("Decimal to Hexadecimal",hex(b))
# Decimal to Hexadecimal -> 102 keep dividing this number by 16, take the reminder from bottom to top.

print("Octal to Hexadecimal",hex(c))
# Octal to Decimal -> 1*8^2 + 0*8^1 + 2*8^0 = 66
# Decimal to Hexadecimal -> 66 keep dividing this number by 16, take the reminder from bottom to top.

