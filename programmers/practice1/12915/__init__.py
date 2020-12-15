# def solution(strings, n):
#     answer = []
#     l = []
#     l2 = []
#     # 2차원 배열로 만들어주는 것 [['sun'], ['bed'], ['car']]
#     # answer = [[x] for x in strings]
#     # [['s', 'u', 'n'], ['b', 'e', 'd'], ['c', 'a', 'r']]
#     for i in strings:
#         l.append(list(i))
#     # ['a', 'e', 'u']
#     for i in range(len(strings)):
#         l2.append(l[i][n])
#         l2.sort()
#     for i in range(len(l2)):  # 0--2
#         for j in range(len(strings)):  # 0--2
#             if l[j][n] == l2[i]:
#                 answer.append(''.join(l[j]))
#                 if answer.index(''.join(l[j])):
#                     del answer[-1]
#                 else: continue
#                 print(answer)
#     return answer

# sun, bed, car
def solution(strings, n):
    # check = [usun, ebed, acar]
    check = []
    answer = []
    for i in strings:
        check.append(i[n] + i)

    strings = sorted(check)

    for i in strings:
        answer.append(i[1:])

    return answer


string2 = ["abce", "abcd", "cdx"]
n2 = 2
print(solution(string2, n2))
