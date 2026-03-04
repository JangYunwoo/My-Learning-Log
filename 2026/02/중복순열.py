numbers = [1,2,3,4,5]               # 숫자가 1~5까지 있음
pick_numbers = []                   # 뽑은 숫자 저장하는곳
M = 3                               # 3개를 뽑을거임
pick_numbers2 = [-1] * M

# 중복순열
def perm(count):
    if count == M:                  # 3번 뽑았다면 
        print(pick_numbers)         # picknumbers를 프린트하고 종료
        return
    
    for i in range(len(numbers)):   # 5번을 반복할것, i는 0~4
        pick_numbers.append(numbers[i]) # pichnumbers에 i=0 추가
        perm(count+1)                   # 재귀로 count+1을 대입하고 다시실행
        pick_numbers.pop()
    
    return None

perm(0)
