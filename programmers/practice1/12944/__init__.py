def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer = answer / len(arr)
    return answer


arr = [1, 2, 3, 4]
print(solution(arr))
