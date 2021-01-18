string_num = input()
count_zero = 0  # 0 -> 1
count_one = 0  # 1 -> 0

# 첫 문자가 0이냐 1이냐에 따라 각각의 변수에 1을 추가한다.
# 이것을 해주는 이유는 아래에서 n - 1을 해서 비교를 할 때에 에러가 나서이다
# 인덱스 0 - 1은 제일 마지막 값인 -1인덱스 값과 비교가 되기 때문에
# 문제의 출제의도와 다르게 적용된다
if string_num[0] == '0':
    count_zero += 1
else:
    count_one += 1

# 0번째 인덱스 값은 비교하였으니 1부터 비교한다.
for n in range(1, len(string_num)):
    # 일치하지 않을 때를 찾아서
    if string_num[n - 1] != string_num[n]:
        # 인덱스 값이 '0' 이면 count_zero 에 + 1 을 하고
        if string_num[n] == '0':
            count_zero += 1
        # 인덱스 값이 '1' 이면 count_one 에 + 1 을 해준다.
        else:
            count_one += 1

# 두 변수 중 더 작은 값을 출력한다
print(min(count_zero, count_one))
