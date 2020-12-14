def solution(n):
    return list(map(int, reversed(str(n))))

n2 = 12345
print(solution(n2))