print("int() can convert any integral value like binary, octal, hexadecimal into decimal.")

print("Binary to Decimal Conversion: ")
a=0b11001
print(int(a)) # 1*2^0 + 0*2^1 + 0*2^2 + 1*2^3 + 1*2^4 = 1+0+0+8+16 = 25
print("Octal to Decimal Conversion: ")
b=0O11001
print(int(b))# 1*8^0 + 0*8^1 + 0*8^2 + 1*8^3 + 1*8^4 = 1+0+0+512+4096 = 4609
print("Hexadecimal to Decimal Conversion: ")
c=0xaf
print(int(c)) # f*16^0 +a*16^1 = 15*16^0 + 10*16^1 = 175
print("Float to Decimal:")
print(int(123.001932))
print(int(12345678901e-7)) # 12345678901 * 10 ^ -7 =1234
print(int(12345678901e-8)) # 12345678901 * 10 ^ -8 =123
print(int(12345678901e-9)) # 12345678901 * 10 ^ -9 =12
print("Boolean to Integer")
print(int(True))
print(int(False))