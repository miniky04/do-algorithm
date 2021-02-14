def solution(phone_number):
    answer = ''
    l = list(phone_number)
    # print(l) #['0', '1', '0', '3', '3', '3', '3', '4', '4', '4', '4']
    # print(l[:-4]) #['0', '1', '0', '3', '3', '3', '3']
    l[:-4] = '*' * len(l[:-4])
    # print(l) #['*', '*', '*', '*', '*', '*', '*', '4', '4', '4', '4']
    answer = ''.join(l)
    return answer


phone_number2 = "01033334444"
print(solution(phone_number2))
