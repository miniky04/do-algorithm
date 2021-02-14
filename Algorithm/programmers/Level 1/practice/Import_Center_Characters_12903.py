def solution(s):
    answer = ""
    n = list(s)
    a = int(len(n)/2) + 1   # 3
    if len(s) % 2 == 1:
        answer = n[a-1]
    else:
        answer = n[a-2] + n[a-1]    # a 의 값이 홀수기준이니 조심
        # 리스트 슬라이싱 사용 x -> []값으로 반환된다.
    return answer


s2 = "abcd"
print(solution(s2))
