num_array = []

for i in range(int(input())):  # 0~4
    num = int(input())
    num_array.append(num)

num_array.sort()

for n in num_array:
    print(n)

