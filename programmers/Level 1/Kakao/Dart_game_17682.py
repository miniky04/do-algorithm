def solution(dartResult):
    total = []
    list_dart = list(dartResult)
    basket = []
    for i in range(len(list_dart)):
        if list_dart[i] == '1' and list_dart[i + 1] == '0':
            basket.append('10')
        elif list_dart[i] == '0' and list_dart[i - 1] == '1':
            continue
        else:
            basket.append(list_dart[i])
    for i in range(1, len(basket)):
        if basket[i] == 'S':
            total.append(int(basket[i - 1]) ** 1)
        elif basket[i] == 'D':
            total.append(int(basket[i - 1]) ** 2)
        elif basket[i] == 'T':
            total.append(int(basket[i - 1]) ** 3)

        if basket[i] == '*':
            if len(total) >= 2:
                total[-1] = total[-1] * 2
                total[-2] = total[-2] * 2
            else:
                total[-1] = total[-1] * 2
        elif basket[i] == '#':
            total[-1] = total[-1] * (-1)
    return sum(total)


dart = "1D2S#10S"
print(solution(dart))

# def solution(dartResult):
#     answer = 0
#     # dart_list = list(str(dartResult))
#     # num = []
#     # print(dart_list) ['1', 'S', '2', 'D', '*', '3', 'T']
#     # for i in range(len(dart_list)):
#     #     if dart_list[i].isdigit():            num.append(dart_list[i])
#     #         if dart_list[i+1] == 'S':
#     #             answer += num[0] ** 1
#     #             del num[0]
#     #         elif dart_list[i+1] == 'D':
#     #             answer += num[0] ** 2
#     #             del num[0]
#     #         elif dart_list[i+1] == 'T':
#     #             answer += num[0] ** 3
#     #             del num[0]
#     return answer


# def solution(dartResult):
#     answer = 0
#     ldart = list(dartResult)
#     dart_num = []
#     for i in range(len(ldart)):
#         if ldart[i] == '*':
#             dart_num.append('*')
#         elif ldart[i] == '#':
#             dart_num.append('#')
#         elif ldart[i] == 'S':
#             dart_num.append(int(ldart[i - 1]) ** 1)
#         elif ldart[i] == 'D':
#             dart_num.append(int(ldart[i - 1]) ** 2)
#         elif ldart[i] == 'T':
#             dart_num.append(int(ldart[i - 1]) ** 3)
#     # print(dart_num) #[1, 4, '*', 27]
#     # print(dart_num) # [1, '*', 8, '*', 3]
#     d = {}
#     for i, j in enumerate(dart_num):
#         d.setdefault(j, []).append(i)
#     dart_index = d.get('*')  # == print(list(d.values())[1])
#     dart_count = len(dart_index)
#     if dart_count == 1 and dart_index[0] == 1:  # '*'가 하나이고 인덱스 값이 1인 경우
#         answer += dart_num[dart_index[0] - 1] * 2
#         print('1:', answer)
#     elif dart_count == 1 and dart_index[0] > 1:  # '*'가 하나이고 인덱스 값이 1 이상인 경우
#         answer += dart_num[dart_index[0] - 1] * 2
#         answer += dart_num[dart_index[0] - 2] * 2
#         print(dart_num)
#         print('2:', answer)
#     elif dart_count > 1:  # '*'가 두 개 이상인 경우
#         dart_num.append(dart_num[dart_index[0] - 1] * 2 * 2)
#         dart_num.append(dart_num[dart_index[1] - 1] * 2)
#         a, b = dart_index[0] - 1, dart_index[1] - 1
#         del dart_num[b]
#         del dart_num[a]
#         dart_num.remove('*')
#         dart_num.remove('*')
#         for i in range(len(dart_num)):
#             answer += dart_num[i]
#         print('3:', answer)
#     else:  # 옵션이 없는 경우
#         for i in range(len(dart_num)):
#             answer += dart_num[i]
#         print('4:', answer)
#     return answer
#
#
# '''
# from collections import defaultdict
#
# d = defaultdict(list)
# for i, j in enumerate(dart_num):
#     d[j].append(i)
# overlap = {key: value for key, value in d.items() if len(value) > 1}
# print(overlap) # {'*': [1, 3]}
# '''
