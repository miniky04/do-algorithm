b1 = bin(97)  # 0b11000001
b2 = bin(98)  # 0b11000010
ret1 = b1 + b2
print(ret1)  # 0b110000010b11000010

a = int(b1, 2)
b = int(b2, 2)
ret2 = a + b
print(bin(ret2))  # 0b11000011
