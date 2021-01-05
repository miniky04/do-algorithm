def solution(s):
    # sorted() 와 sort() 개념 정리해두기
    list_num = sorted(map(int, s.split(' ')))
    return str(list_num[0]) + ' ' + str(list_num[-1])


m = "-2 5 -9 7 10 -25"
print(solution(m))
