for j in range(10):
    N = int(input())
    floor = list(map(int, input().split()))
     
    result = 0
 
    i = 2
    while i <= len(floor) - 2:
        if max(floor[i-2:i+3]) == floor[i]:
            A = sorted(floor[i-2:i+3])
            result += A[-1] - A[-2]
            i += 3
        else:
            i += 1
 
    print(f"#{j+1} {result}")