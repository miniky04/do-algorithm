def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        if s.isdigit(): #문자열이 숫자인지 확인하는 함수
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer


s2 = "123256"
print(solution(s2))