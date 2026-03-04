T = int(input())
 
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
 
    numbers.sort()
 
    print(f"#{tc+1}", end=" ")
    print(" ".join(map(str, numbers)))