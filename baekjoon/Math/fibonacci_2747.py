import sys

f0 = 0
f1 = 1
total = 0
num = int(sys.stdin.readline())

for i in range(num):
    total = f0 + f1
    f0 = f1
    f1 = total

print(f0)
