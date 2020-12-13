def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
        else:
             continue
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer) #원본배열 순서가 변하지않고 유지된다.


# def solution(arr, divisor):
#     answer = list(filter(lambda x: x % divisor == 0, arr))
#     return sorted(answer) if len(answer) > 0 else [-1]


arr2 = [2,36,1,3]
div = 1
print(solution(arr2, div))
