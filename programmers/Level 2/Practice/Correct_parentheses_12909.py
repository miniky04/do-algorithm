def solution(s):
    answer = True
    array = []
    for i in s:
        if i == '(':
            array.append(i)
        elif i == ')':
            if len(array) > 0:
                array.pop()
            elif len(array) == 0:
                answer = False
                break
    if answer:
        if len(array) > 0:
            answer = False
        else:
            answer = True
    return answer


# 아마 이 코드가 내 생각에 배우고싶은 코드였을거야 응
# def is_pair(s):
#     # 함수를 완성하세요
#     x = 0
#     for w in s:
#         if x < 0:
#             break
#         x = x+1 if w=="(" else x-1 if w==")" else x
#     return x==0


n3 = ")()("
print(solution(n3))
