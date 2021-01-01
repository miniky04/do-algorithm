# def solution(a, b):
#     return (str('*' * a) + '\n') * b
#
#
# a2, b2, = 5, 3
# print(solution(a2, b2))


a, b = map(int, input().strip().split(' '))
print((str('*' * a) + '\n') * b)
