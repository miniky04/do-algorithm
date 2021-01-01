def solution(x, n):
    answer = [x]
    for i in range(1, n):
        answer.append(x+(x*i))
    return answer


x2 = -4
n2 = 2
print(solution(x2, n2))