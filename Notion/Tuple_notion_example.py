tuple1 = (10, 11, 12)
tuple2 = ('b', 'c', 'f')
tuple3 = (1, 'abc', 'd', [5, 8, 3], ['a', 'c'])

'''
tuple1[0] = 0
TypeError: 'tuple' object does not support item assignment
튜플의 요소는 그 값을 변경할 수 없다.
'''


def func():
    print("hello world")


tuple4 = (1, 'a', func)
tuple4[2]()  # hello world
