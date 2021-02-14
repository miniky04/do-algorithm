import sys

num = int(sys.stdin.readline())
count = 0

while num > 1:
    num -= 1
    count += 1
    if num % 3 == 0:
        num = num // 3
        count += num // 3
    if num % 2 == 0:
        num = num // 2
        count += num // 2

print(count)
