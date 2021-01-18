from typing import List

n = int(input())
for i in range(n):
    if i == 0:
        array = list(input())
    else:
        array_two = list(input())
        for j in range(len(array)):
            if array[j] != array_two[j]:
                array[j] = '?'

print(''.join(array))