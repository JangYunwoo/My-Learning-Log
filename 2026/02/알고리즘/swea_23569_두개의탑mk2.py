T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    block = list(map(int, input().split()))

    A_top = []
    B_top = []
    
    block.sort()

    result = 0

    for _ in range(min([A,B])):
        A_top.append(block.pop())
        B_top.append(block.pop())

    if A != B:
        for _ in range(abs(B-A)):
            A_top.append(block.pop())

    for i in range(1,len(A_top)+1):
         result += i*A_top[i-1]
    for i in range(1,len(B_top)+1):
         result += i*B_top[i-1]

    print(f"#{tc} {result}")