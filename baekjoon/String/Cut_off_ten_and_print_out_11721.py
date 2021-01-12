seq = input()
length = 10
s = [seq[i: i + length] for i in range(0, len(seq), length)]
for j in range(len(s)):
    print(''.join(s[j]))
