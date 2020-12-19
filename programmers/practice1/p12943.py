def solution(num):
    answer = 0
    a = True
    while a:
        if num > 1:
            if answer > 500:
                return -1
            elif num % 2 == 0:
                num = num / 2
                answer += 1
            elif num % 2 == 1:
                num = num * 3 + 1
                answer += 1
        elif num == 1:
            a = False
            return answer
    return answer


n2 = 16
print(solution(n2))