import sys

dwarf_list = []
breaker = False

for i in range(9):
    dwarf = int(sys.stdin.readline())
    dwarf_list.append(dwarf)

sum_dwarf = sum(dwarf_list)

for i in range(9):
    for j in range(9):
        if i != j and sum_dwarf - dwarf_list[i] - dwarf_list[j] == 100:
            a, b = dwarf_list[i], dwarf_list[j]
            dwarf_list.remove(a)
            dwarf_list.remove(b)
            breaker = True
            break
    if breaker:
        break

dwarf_list = sorted(dwarf_list)

for x in range(7):
    print(dwarf_list[x])
