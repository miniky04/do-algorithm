import sys

total = 0
odd_list = []
even = 0

for i in range(7):
    num = int(sys.stdin.readline())
    if num % 2 == 1:
        total += num
        odd_list.append(num)
    else:
        even += 1

if even == 7:
    print(-1)
else:
    odd_list.sort()
    print(total, odd_list[0])
