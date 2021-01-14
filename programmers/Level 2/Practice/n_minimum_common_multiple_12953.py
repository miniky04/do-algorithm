def solution(arr):
    # p는 이전 값
    p = arr[0]
    for i in range(1, len(arr)):
        # 이전 값인 p와 최소공배수 구하는 것
        p = p * arr[i] // gcd(p, arr[i])
    return p


# 최대공약수 구하는 함수
def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)


l = [2, 6, 8, 14]
print(solution(l))
