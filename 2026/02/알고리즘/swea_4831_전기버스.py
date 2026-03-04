T = int(input())
 
for i in range(T):
    K, N, M = map(int, input().split())
    elecstop = list(map(int, input().split()))
 
    result = 0
 
    k = 0
    k_test = 0
    while k < N:
        k_test += K
        if k_test >= N:
            break
        else:
            while k_test > k:
                if k_test not in elecstop:
                    k_test -= 1
                else:
                    k = k_test
                    result += 1
                    break
            else:
                result = 0
                break
     
    print(f"#{i+1} {result}")