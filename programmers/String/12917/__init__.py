# def solution(s):
#     answer = []
#     answer = ''.join(list(sorted(s))[::-1])
#     return answer

#최적화 코드
def solution(s):
    return ''.join(sorted(s, reverse=True))


s2 = "Zagcedf"
print(solution(s2)) #gfedcaZ
