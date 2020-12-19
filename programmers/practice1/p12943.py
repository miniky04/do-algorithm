def solution(num):
    answer = 0
    a = True
    while a:
        if num > 1:
            # 500이 넘으면 -1 반환
            if answer > 500:
                return -1
            # 짝수일 때
            elif num % 2 == 0:
                num = num / 2
                answer += 1
            # 홀수일 때
            elif num % 2 == 1:
                num = num * 3 + 1
                answer += 1
        # 1이 된다면 while구문 그만 반복하고 answer값 반환
        elif num == 1:
            a = False
            return answer
    return answer


n2 = 16
print(solution(n2))
