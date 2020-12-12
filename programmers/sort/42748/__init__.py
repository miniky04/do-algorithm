array2 = [1, 5, 2, 6, 3, 7, 4]
commands2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for command in commands: #command = [2,5,3]
        array3 = array[command[0]-1:command[1]] #array3 = [5,2,6,3]
        array3.sort() #array3 = [2,3,5,6]
        answer.append(array3[command[2]-1])
    return answer


print(solution(array2, commands2))
