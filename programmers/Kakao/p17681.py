def solution(n, arr1, arr2):
    binary_list = []
    for i in range(n):
        binary = arr1[i] | arr2[i]
        binary2 = str(bin(binary)[2:])
        binary2 = binary2.zfill(n)
        binary_list.append(binary2.replace('1', '#').replace('0', ' '))
    return binary_list


n2 = 5
a = [9, 20, 28, 18, 11]
a2 = [30, 1, 21, 17, 28]
print(solution(n2, a, a2))

# 내가 진짜 인생살면서 코드를 길게 쓸 필요가 없어졌다는 걸 너가 나중에 밑에 코드를 보면 느낄거다
# binary = []
# binary2 = []
# for i in arr1:
#     b = str(bin(i)[2:])
#     binary.append(str(b.zfill(5)))
# # print(binary) ['01001', '10100', '11100', '10010', '01011']
# for i in arr2:
#     b2 = str(bin(i)[2:])
#     binary2.append(str(b2.zfill(5)))
# # print(binary2) ['11110', '00001', '10101', '10001', '11100']
# for i in range(n):
#     arr_or = arr1[i] | arr2[i]
#     print(arr_or)
#     b3 = str(bin(arr_or)[2:])
#     print(b3)
