numbers = [1,2,3,4,5]
pick_numbers = []
M = 3
pick_numbers2 = [-1] * M

# 순열
visited = [0]*len(numbers)          # [0,0,0,0,0]
def perm2(count):
    if count == M:
        print(pick_numbers2)
        return
    
    for i in range(len(numbers)):   # i = 0,1,2,3,4
        if visited[i] == 0:         # vis[i]가 0이면
            visited[i] = 1          # vis[i]를 1로 바꿈
            pick_numbers2[count] = numbers[i]   #pick2의 첫번째 숫자 = 1
            perm2(count+1)              #pick2의 두전째숫자 실행
            visited[i] = 0

perm2(0)

# [1,]일때 두번째 숫자에서 i=0이라면 진행되지 않음, i=1로 넘어감. [1,2] 