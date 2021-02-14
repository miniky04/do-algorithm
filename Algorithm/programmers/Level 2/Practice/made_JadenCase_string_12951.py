def solution(s):
    split_list = s.split(' ')
    for i in range(len(split_list)):
        split_list[i] = split_list[i].capitalize()
    return ' '.join(split_list)


a = "3people unFollowed me"
print(solution(a))
