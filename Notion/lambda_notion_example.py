# lambda 인자리스트 : 표현식
g = lambda x: x ** 2
print(g(8))  # 64

f = lambda x, y: x + y
print(f(4, 4))  # 8


# lambda function use
def inc(n):
    return lambda x: x + n


f = inc(2)
g = inc(4)
print(f(12))
print(g(12))
print(inc(2)(12))


def add(n, m):
    return n + m


print(add(2, 3))  # 5
# 이것을 lambda로 하면?
print((lambda n, m: n + m)(2, 3))

# 람다를 변수에 할당하여 재사용하기
lambdaAdd = lambda n, m: n + m
print(lambdaAdd(2, 3))  # 5
print(lambdaAdd(4, 5))  # 9

# 람다식 안에서 if 구문 사용하기
print((lambda n, m: n if n % 2 == 0 else m)(1, 3))  # 3
print((lambda n, m: n if n % 2 == 0 else m)(2, 3))  # 2

# map()함수와 함께 사용되는 lambda -> map() 내장함수
# r = map(function, iterable, ...)
# iterable 은 한번에 하나의 멤버를 반환할 수 있는 객체
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
list(map(lambda x, y: x + y, a, b))  # [18,14,14,14]

map(lambda x: x ** 2, range(5))  # [0,1,4,9,16]
list(map(lambda x: x ** 2, range(5)))  # [0,1,4,9,16]
# 위와 아래의 차이점은 아래는 함수를 적용시킨 결과를 새로운 리스트에 담는다.

# filter()함수와 함께 사용되는 lambda -> filter() 내장함수
# r = filter(function, iterable)
# filter에 인자로 사용되는 function은 처리되는 각각의 요소에 대해 Boolean값을 반환
# True -> 요소는 남고 False -> 요소 제거
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
list(filter(lambda x: x % 3 == 0, foo))  # [18,9,24,12,27]

filter(lambda x: x < 5, range(10))  # [0,1,2,3,4]
list(filter(lambda x: x < 5, range(10)))  # [0,1,2,3,4]

filter(lambda x: x % 2, range(10))  # [1,3,5,7,9]
list(filter(lambda x: x % 2, range(10)))  # [1,3,5,7,9]

# reduce()함수와 함께 사용되는 lambda
# functools.reduce(function, iterable[, initializer])
# reduce()함수를 두 개의 필수 인자와 하나의 옵션 인자를 가지는데, function을
#  사용해서 inerable을 하나의 값으로 줄입니다. initializer는 주어지면 첫번째
#  인자로 추가된다고 생각하면 된다.
from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15

reduce(lambda x, y: y + x, 'abcde')  # 'edcba'
# (a)(b)cde - (ba)(c)de - (cba)(d)e - (dcba)(e) - (edcba)
