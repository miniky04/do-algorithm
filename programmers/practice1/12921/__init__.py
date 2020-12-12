import math


def solution(n):
    arr = [True] * (n + 1) #arr 배열 안의 값은 다 True로 입력되어있다
    arr[1] = False
    count = 0
    for i in range(2, n + 1):
        if arr[i]:
            if isPrimeNumber(i):
                count += 1
                for j in range(i * 2, n + 1, i): #2 -> 4,10,2
                    arr[j] = False #j 가 i의 배수 -> j의 약수중에 i가 있다.
    return count


def isPrimeNumber(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0: #i가 n의 약수다
            return False
    return True


n2 = 5
print(solution(n2))

#에라토스테네스 풀이법 !
#이 코드는 2번의 최적화가 이루어졌다.