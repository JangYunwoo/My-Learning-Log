T = int(input())
 
for i in range(T):
    A = []
    for j in range(9):
        A.append(list(map(int, input().split())))
 
    result = 1
 
    for j in range(9):
        if len(list(set(A[j]))) != 9:
            result = 0
            break
    if result == 0:
        print(f"#{i+1} {result}")
        continue
 
    for j in range(9):
        if len(list(set([A[k][j] for k in range(9)]))) != 9:
            result = 0
            break
    if result == 0:
        print(f"#{i+1} {result}")
        continue
 
    for j in range(3):
        for k in range(3):  #(A[0][0:2] + A[1][0:2] + A[2][0:2]), (A[0][3:5] + A[1][3:5] + A[2][3:5])
            if len(list(set(A[j*3][3*k:3*k+3] + A[j*3+1][3*k:3*k+3] + A[j*3+2][3*k:3*k+3]))) != 9:
                result = 0
                break
    if result == 0:
        print(f"#{i+1} {result}")
        continue
    print(f"#{i+1} {result}")