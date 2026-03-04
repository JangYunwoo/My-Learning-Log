from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    lst = input()

    D_count = p.count('D')
    R_count = len(p)-D_count
    if D_count > n:
        print('error')
        continue
    elif D_count == n:
        print([])
        continue
    
    lst = deque(map(int, lst[1:-1].split(',')))
    switch = 0
    for i in p:
        if i == 'R':
            switch = (switch+1)%2
        else:
            if switch == 0:
                lst.popleft()
            else:
                lst.pop()

    if R_count % 2 == 0:
        print('[' + ','.join(map(str, list(lst))) + ']')
    else:
        print('[' + ','.join(map(str, list(lst)[-1::-1])) + ']')
