a=0b101010101
b=102
c=0x1021

print("Binary to Octal: ", oct(a))
# right to left -> 101(5) 010(2) 101(5)

print("Decimal to Octal: ",oct(b))
# Keep dividing the number by 8 till your reach the value to 0. While dividing , arrange all the reminders from Bottom to Top

print("Hexadecimal to Octal: ", oct(c))
# 1*16^3 + 0*16^2 + 2*16^1 + 1*16^0=4129
# 4129 -> Keep dividing by 8 and whatever reminder you get, read teh reminder from bottom to top.
# 10041 