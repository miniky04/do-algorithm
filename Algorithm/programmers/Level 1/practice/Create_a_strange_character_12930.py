# def solution(s):
#     answer = ''
#     l = list(s)
#     for i in range(1, len(s) + 1):
#         if i % 2 == 1:
#             answer += ''.join(l[i - 1].upper())
#         elif i % 2 == 0:
#             answer += ''.join(l[i - 1].lower())
#         else:
#             answer += ''.join(l[i - 1])
#     return answer


# def solution(s):
#     answer = ""
#     # print(list(s))
#     a = list(s.split(' '))  # ['try', 'hello', 'world']
#     for i in a:
#         b = list(str(i))
#         for j in range(len(b)):
#             if j == 0:
#                 answer += b[j].upper()
#             elif j % 2 == 0:
#                 answer += b[j].upper()
#             elif j % 2 == 1:
#                 answer += b[j].lower()
#             else:
#                 answer += b[j]
#         answer += ' '
#     return answer.strip()


# import time


def solution(s):
    # start_time = time.time()
    answer = ''
    a = s.split(' ')  # ['try', 'hello', 'world']
    for i in a:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    # print(time.time() - start_time)
    return answer[:-1]

#위보단 아래가 더 효율적 !
# def solution(s):
#     temp_list = []
#     new_s = s.split(' ')
#     for word in new_s:
#         size = len(word)
#         for i in range(size):
#             if i % 2 == 0:
#                 temp_list.append(word[i].upper())
#             else:
#                 temp_list.append(word[i].lower())
#
#         temp_list.append(' ')
#     answer = ''.join(temp_list)
#     return answer[:-1]


ans = "try hello world"
print(solution(ans))
