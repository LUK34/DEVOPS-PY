print(complex(102)) # 102 + 0j
print("Binary -> Decimal -> Complex")
print(complex(0b10101)) # 1*2^0 + 0*2^1 + 1*2^2 + 0*2^3 + 1*2^4= 1+0+4+0+16 = 21 -> 21 +0j
print("Octal -> Decimal -> Complex")
print(complex(0o10101))# 1*8^0 + 0*8^1 + 1*8^2 + 0*8^3 + 1*8^4 = 1+0+64+0+4096 = 4161 -> 4161 + 0j
print("Hexadecimal -> Decimal -> Complex")
print(complex(0xaf)) # f*16^0 +a*16^1 = 15*16^0 + 10*16^1 = 175 -> 175 + 0j
print("Float -> Complex")
print(complex(1.0003))
print("Boolean -> Complex")
print(complex(True))
print("String -> Complex")
print(complex('1101'))

