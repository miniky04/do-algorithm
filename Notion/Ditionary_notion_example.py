dict1 = {'a': 1, 'c': 3, 'e': 5}
print(dict1['c'])  # 3

dict1['z'] = 26  # 값 추가
print(dict1)  # {'a': 1, 'c': 3, 'e': 5, 'z': 26}

dict1['a'] = 0  # 값 변경
print(dict1)  # {'a': 0, 'c': 3, 'e': 5, 'z': 26}

print(len(dict1))  # 4
