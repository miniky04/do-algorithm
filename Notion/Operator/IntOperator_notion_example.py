bnum = 0b11110000
bstr = '0b11110000'
onum = 0O360
ostr = '0O360'
hnum = 0xf0
hstr = '0xf0'

# b2 = int(bstr, 0)
b1 = int(bnum)
b2 = int(bstr, 2)
# o2 = int(ostr, 0)
o1 = int(onum)
o2 = int(ostr, 8)
# h2 = int(hstr, 0)
h1 = int(hnum)
h2 = int(hstr, 16)

# b1 :  240 , b2 :  240
print("b1 : ", b1, ", b2 : ", b2)
# o1 :  240 , o2 :  240
print("o1 : ", o1, ", o2 : ", o2)
# h1 :  240 , h2 :  240
print("h1 : ", h1, ", h2 : ", h2)
