from collections import deque

for _ in range(1, 11):
    tc = input()
    data = deque(map(int, input().split()))

    i = 1
    while True:
        a = data.popleft() - i
        if a > 0:
            data.append(a)
        else:
            data.append(0)
            break
        i = i%5+1
    print('#' + tc, *data)