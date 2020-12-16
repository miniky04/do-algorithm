def solution(n):
    answer = 0
    l = list(str(n))  # ['1','2','3']
    l2 = list(map(int, l))
    # print(l2) [1, 2, 3]
    for i in range(len(l)):
        answer += l2[i]
    return answer


n2 = 123
print(solution(n2))
