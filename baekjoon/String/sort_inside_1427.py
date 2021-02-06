import sys

num = int(sys.stdin.readline())
print(''.join(sorted(str(num), reverse=True)))

