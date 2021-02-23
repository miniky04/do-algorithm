h1 = hex(97)  # 0x61
h2 = hex(98)  # 0x62
ret1 = h1 + h2  # 0x610x62

a = int(h1, 16)
b = int(h2, 16)
ret2 = a + b  # 195

print(hex(ret2))  # 0xc3
