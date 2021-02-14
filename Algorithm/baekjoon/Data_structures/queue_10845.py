import sys

queue = []

for i in range(int(sys.stdin.readline())):
    scan = sys.stdin.readline().split()
    if scan[0] == 'push':
        queue.append(int(scan[1]))
    elif scan[0] == 'pop':
        if len(queue) > 0:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif scan[0] == 'size':
        print(len(queue))
    elif scan[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif scan[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif scan[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
