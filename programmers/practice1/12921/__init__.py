import math


def solution(n):
    arr = [True] * (n + 1)
    arr[1] = False
    count = 0
    for i in range(2, n + 1):
        if arr[i]:
            if isPrimeNumber(i):
                count += 1
                for j in range(i * 2, n + 1, i):
                    arr[j] = False
    return count


def isPrimeNumber(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


n2 = 5
print(solution(n2))
