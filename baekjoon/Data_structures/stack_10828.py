import sys

stack = []

for i in range(int(sys.stdin.readline())):
    scan = sys.stdin.readline().split()
    if scan[0] == 'push':
        stack.append(int(scan[1]))
    elif scan[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif scan[0] == 'size':
        print(len(stack))
    elif scan[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif scan[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
