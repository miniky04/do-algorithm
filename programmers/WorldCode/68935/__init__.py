def solution(n):
    answer = 0
    l = []
    while n > 0:
        l.append(n % 3)
        n //= 3
    l = l[::-1]  # [0,0,2,1] 을 [1,2,0,0] 으로 바꾸어줌
    l = l[::-1]  # [1,2,0,0] 을 [0,0,2,1]로 바꾸어줌
    j = len(l)
    for i in range(len(l)):
        answer += l[i] * (3 ** (j - 1))
        j -= 1
    return answer


n2 = 125
print(solution(n2))
