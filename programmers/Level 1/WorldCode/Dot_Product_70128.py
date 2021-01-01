def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


a2 = [-1, 0, 1]
b2 = [1, 0, -1]
print(solution(a2, b2))
