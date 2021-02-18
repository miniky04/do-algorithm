list1 = [1, 2, 3]
list2 = ['a,', 'b', 'c']
list3 = ['abc', 'a', '1', [1, 2, 3], ['a', 'b']]

list1[0] = 5  # 값 변경하기
print(list1)  # list1 = [5, 2, 3]


def func():
    print('hello world')


list4 = [1, 'a', func]
list4[2]()  # hello world
