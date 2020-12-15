def solution1(n, m):
    answer = []
    d = []
    d2 = []
    d3 = []
    for i in range(1, n + 1):
        if n % i == 0:  # 3 / 1 = 3 # 3 / 3 = 1
            d.append(i)
    # print(d)
    for i in range(1, m + 1):
        # 1 2 3 4 6 12
        if m % i == 0:
            d2.append(i)
    # print(d2)
    for i in d:
        for j in d2:
            if i == j:
                d3.append(i)
    # print(d3) -> 1, 3
    max_d = max(d3)  # 최대공약수
    # print(max_d)
    min_d = n * m / max_d
    answer.append(max_d)
    answer.append(int(min_d))
    return answer

def solution(n, m):
    max_d = gcd(m, n)
    min_d = n * m / max_d
    return [max_d, min_d]


def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)


n2 = 24
m2 = 16
print(solution(n2, m2))
