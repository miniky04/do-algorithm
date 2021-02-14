def solution(n):
    answer = ""
    s = list(map(int, sorted(list(str(n)), reverse=True)))
    for i in range(len(list(str(n)))):
        answer += str(s[i])
    answer = int(answer)
    return answer


n2 = 118372
print(solution(n2))