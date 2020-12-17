def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget-i >= 0:
            budget -= i
            answer += 1
        else:
            break
    return answer


d2 = [1, 3, 2, 5, 4]
budget2 = 9
print(solution(d2, budget2))
