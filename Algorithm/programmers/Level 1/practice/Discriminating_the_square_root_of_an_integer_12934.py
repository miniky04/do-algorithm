import math


def solution(n):
    num = math.sqrt(n)
    if int(num) == num:
        return int(math.pow(num + 1, 2))
    return -1


a = 121
print(solution(a))
