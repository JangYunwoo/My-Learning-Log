T = int(input())
 
for i in range(T):
    N, M = map(int, input().split())
 
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    result = "YES"
 
    try:
        for _ in range(len(B)):
            del A[:A.index(B[0])+1]
            B.pop(0)
    except ValueError:
        result = "NO"
 
    print(f"#{i+1} {result}")