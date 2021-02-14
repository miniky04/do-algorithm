def solution(arr):
    answer = []
    if len(arr) < 2:
        answer.append(-1)
    else:
        min1 = arr[0]
        index1 = 0
        # 최솟값 구하기
        for i in range(len(arr)):
            if arr[i] < min1:
                min1 = arr[i]  # 값
                index1 = i  # 값의 위치
        # print(min1) = 1
        del arr[index1]
        answer = arr
    return answer

    # answer = 0
    # smallest = arr[0]
    # if len(arr) < 2:
    #     answer = [-1]
    # for i in arr:
    #     if i < smallest:
    #         smallest = i
    #         continue
    #     m = arr.index(smallest)
    #     del arr[m]
    # answer = arr


arr2 = [5, 4, 3, 2, 1]
print(solution(arr2))
