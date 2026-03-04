# 초기 입력 문자열, 그리고 그 길이 N
set_str = list(input())
N = len(set_str)

# 받을 명령어 개수
M = int(input())

# 명령어 개수만큼 반복
for _ in range(M):
    # split을 사용해서 받는 개수에 상관없이 list로 변환
    order = input().split()

    if order[0] == 'L':
        if N > 0:   # order가 L이면 커서의 현 위치가 되는 N 왼쪽으로 이동
            N -= 1  # 근데 커서가 맨 왼쪽에 있으면 움직이지 않음
    elif order[0] == 'D':
        N += 1  # D면 오른쪽으로 이동
    elif order[0] == 'B':
        if N > 0:   # 이 if설정은 'L'을 받을때와 같음
            set_str.pop(N-1)    # 'abcd'를 받았다면 커서의 현 위치는 4이므로 여기서 B를 받게되면 index가 3인 문자열을 지워야하므로 N-2:N-1을 사용
            N -= 1              # str형식의 경우 불변형이라 중간 index를 제거하고 덮어씌우는건 어려우므로 set_str을 list로 받음
                            # 이러면 pop 메서드를 사용하기 용이하므로 N-2:N-1에서 pop으로 변환하고 N=4일때 index 3을 없애야 하므로
                            # pop(N-1)로 사용
                            # 마지막으로 커서의 왼쪽을 지웠으므로 커서가 왼쪽으로 이동하게됨. 즉 커서의 위치가 1 줄어듬
    else:       #남은건 order[0]이 "P"일 경우
        set_str.insert(N,order[1]) # 비슷한 흐름으로 P로 입력을 하면 현재 커서 위치(N)에 추가할 문자열, 즉 order[1]을 insert로 추가
        N += 1                       # pop의 N-1과는반대의 경우로 입력하면 커서가 오른쪽으로 이동하게 되므로 위치 N이 1 증가

#작업이 끝나면 list 형식 안에 str형식 문자열만 존재하므로 join을 자용해서 출력
print(''.join(set_str))