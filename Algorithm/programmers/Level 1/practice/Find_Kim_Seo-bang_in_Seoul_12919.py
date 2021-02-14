def solution(seoul):
    n = seoul.index("Kim")
    answer = "김서방은 {}에 있다".format(n)
    return answer


seoul2 = ["Jane", "Kim"]
print(solution(seoul2))