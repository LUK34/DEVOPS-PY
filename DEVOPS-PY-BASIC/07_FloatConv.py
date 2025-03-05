print(float(10229))
print("Binary -> Decimal -> Float")
print(float(0b10101))# 1*2^0 + 0*2^1 + 1*2^2 + 0*2^3 + 1*2^4 = 1+0+4+0+16 = 21 -> 21.0
print("Octal -> Decimal -> Float")
print(float(0o10101))# 1*8^0 + 0*8^1 + 1*8^2 + 0*8^3 + 1*8^4 = 1+0+64+0+4096 = 4161 -> 4161.0
print("Hexadecimal -> Decimal -> Float")
print(float(0xaf)) # f*16^0 +a*16^1 = 15*16^0 + 10*16^1 = 175 -> 175.0

