import sys


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


t = int(sys.stdin.readline())
for i in range(t):
    num = int(sys.stdin.readline())
    print(fibonacci(num))
