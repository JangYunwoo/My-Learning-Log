from collections import deque
import math
import sys

input = sys.stdin.readline


N = int(input())
poop = list(map(int, input().split()))
k, perm  = poop[0], poop[1:]
numbers = [(i+1) for i in range(N)]

if k == 1:
    result = deque()
    perm = perm.pop() - 1
    for i in range(N):
        a = numbers[perm // math.factorial(N-i-1)] # 3 // 6 = 0, 3 // 2 = 1
        result.append(a) # 1, 3
        numbers.remove(a) # 1, 3
        perm %= math.factorial(N-i-1)
    print(*result)


else:
    result = 0
    for i in range(N):
        result += numbers.index(perm[i]) * math.factorial(N-i-1)
        numbers.remove(perm[i])
    print(result+1)