array = [] #2차원 배열로 값을 비교할 때 쓰임
array2 = [] #출력 값 담을 배열
a = True
m = int(input())

for i in range(m): #1차원 배열이 몇개인가에 대한 i
    n = list(input())
    array.append(n)
print(array)

for i in range(m):
    for j in range(len(n)): #2차원 배열 안의 문자열 개수
        if array[i][j] == array[i-1][j] and array[i][j] == array[i][j]:
            array2.append()
        # else:
        #     a = False
        #     break
        # if len(array) > len(array2):
        #     array2.append('?' * (len(array)-len(array2)))

print(str(array2))