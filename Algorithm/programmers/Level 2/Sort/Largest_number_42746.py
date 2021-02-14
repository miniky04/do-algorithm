def solution(numbers):
    num_list = []
    comparison = []
    total = []

    # 수의 길이 구하기
    for i in list(str(numbers)):
        if i.isdigit():
            num_list.append(i)
    num_len = len(num_list)

    # 길이 하나씩 줄여가며 수 만들기
    for i in numbers:
        comparison.append(str(i).ljust(num_len, '9'))
        print("comparison: ", comparison)
        # print(zip(i, comparison))
        total = dict(i=comparison)
        print(total)
        # total.append(max(comparison))
        # print("total :", total)

    return 0


num = [6, 10, 2]
print(solution(num))
