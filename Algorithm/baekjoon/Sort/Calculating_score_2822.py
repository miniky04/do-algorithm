num_array = []
total = 0
index_array = []

for i in range(8):
    num_array.append(int(input()))

for i in range(5):
    total += max(num_array)
    index = num_array.index(max(num_array))
    index_array.append(index + 1)
    num_array[index] = 0

print(total)
print(*(sorted(index_array)))
