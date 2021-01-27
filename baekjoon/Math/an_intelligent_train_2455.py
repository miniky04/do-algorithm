total_list = []
total = 0

for i in range(4):
    down, up = map(int, input().split())
    total = total - down + up
    total_list.append(total)

print(max(total_list))
