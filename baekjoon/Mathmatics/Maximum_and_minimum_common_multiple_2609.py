import sys

a, b = map(int, sys.stdin.readline().split())


# 최대공약수 구하는 함수
def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)


# 최소공배수 구하는 함수
def lcm(n, m):
    return n * m / gcd(n, m)


print(int(gcd(a, b)))
print(int(lcm(a, b)))
