## 링크

https://www.acmicpc.net/problem/2751

## 분류

정렬

## 주의점

int(input()) 을 하니 계속 시간초과가 났다.
이를 해결할려면 아래와 같이 코드를 짜야한다. -> sys.stdin.readline()

```python
import sys

n = int(sys.stdin.readline())
num_basket = []

for i in range(n):
    num = int(sys.stdin.readline())
    num_basket.append(num)
sorted(num_basket)

for j in num_basket:
    print(j)
```