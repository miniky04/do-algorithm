def solution(arr):
    answer = []
    answer.append(arr[0])  # 값을 넣어두고 시작해야 index out of range 에러가 안뜬다
    for i in arr:  # i = 1,1,3,3,0,1,1
        if i != answer[-1]:  # i와 answer에 젤 마지막 값과 비교해서 다르면
            answer.append(i)  # 추가한다
    # l = len(arr)  # 7
    # for i in range(l):  # 0--6
    #     for j in range(l):  # 0--6
    #         if arr[i] == arr[j] and i != j:
    #             answer.append(arr[i])
    #         elif arr[i] != arr[j]:
    #             answer.append(arr[i])
    #         else:
    #             continue
    return answer


arr2 = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr2))
