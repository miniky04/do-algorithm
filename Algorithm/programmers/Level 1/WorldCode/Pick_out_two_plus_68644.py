def solution(n):
    answer = []
    l = len(n)
    for i in range(l):
        for j in range(l):
            if n[i] != n[j]:
                answer.append(n[i] + n[j])
            elif n[i] == n[j] and i != j:
                answer.append(n[i] + n[j])
    # answer = list(set(answer))
    return sorted(list(set(answer)))
    # return list(map(int, sorted(str(n))))


num = [1, 1, 2, 2, 3, 4]
print(solution(num))
