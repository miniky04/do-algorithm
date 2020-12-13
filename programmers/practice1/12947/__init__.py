def solution(n):
    answer = True
    s = 0
    l = list(str(n))
    for i in l:
        s += int(i)
    if n % s == 0:
        answer = True
    else:
        answer = False
    return answer


arr2 = 310
print(solution(arr2))


# s = 0
# for i in range(1, 11):
#     s += i
# print(s)