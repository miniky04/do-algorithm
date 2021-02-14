import sys

num, pair = map(int, sys.stdin.readline().split())

numbers = []
comparison = []

for i in range(num):
    number = int(sys.stdin.readline())
    numbers.append(number)

# print("num:", numbers)

for i in range(pair):
    range_a, range_b = map(int, sys.stdin.readline().split())
    for j in range(range_a-1, range_b):
        # print("j:", j)
        comparison.append(numbers[j])
    # print("com:", comparison)
    print(min(comparison))
    comparison.clear()