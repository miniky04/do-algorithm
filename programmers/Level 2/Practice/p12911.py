def solution(n):
    n_count = bin(n).count('1')
    for i in range(n + 1, 1000001):
        if bin(i).count('1') == n_count:
            return i


m = 78
print(solution(m))
