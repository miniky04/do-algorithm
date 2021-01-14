def solution(n):
    f0, f1 = 0, 1
    for i in range(2, n+1):
        fn = f0
        f0 = f1
        f1 = fn + f1
    return f1 % 1234567


# 0 1 1 2 3 5 8 13 21 44 65 109
a = 3
print(solution(a))
