def solution(A, B):
    answer = 0
    sort_a = sorted(A)
    sort_b = sorted(B, reverse=True)
    len_a = len(A)

    for i in range(len_a):
        answer += sort_a[i] * sort_b[i]
    return answer


a = [1, 4, 2]
b = [5, 4, 4]
print(solution(a, b))
