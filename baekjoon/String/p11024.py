n = int(input())
answer = 0
for i in range(n):
    ns = list(map(int, input().split()))
    for j in range(len(ns)):
        answer += ns[j]
    print(answer)
    answer = 0
