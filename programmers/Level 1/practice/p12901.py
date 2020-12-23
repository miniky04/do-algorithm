def solution(a, b):
    answer = ''
    ml = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    ms = 0
    for i in range(a-1):
        ms += ml[i]
    n = (ms + b + 4) % 7
    #4인 이유는 1월 1일부터 시작해서 (5라고 착각x 1월 0일이 아님)
    answer = day[n]
    return answer

# def getDayName(a,b):
#     months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     return days[(sum(months[:a-1])+b-1)%7]


a1 = 5
b2 = 24
print(solution(a1, b2))
