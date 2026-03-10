import math

def search(count, left, right):
    global result
    if left < right:
        return
    if left != 0 and sum_weight/left <=2:
        result_sub = math.factorial(N-count)*2**(N-count)
        result += result_sub
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            search(count+1, left+weight[i], right)
            search(count+1, left, right+weight[i])
            visited[i] = 0



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    weight = list(map(int, input().split()))

    sum_weight = sum(weight)
    visited = [0]*(N)
    result = 0
    search(0, 0, 0)

    print(f"#{tc} {result}")