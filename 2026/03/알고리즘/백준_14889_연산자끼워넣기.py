from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
o = list(map(int, input().split()))

order_list = []
for i in range(4):
    for _ in range(o[i]):
        order_list.append(i)

max_answer = float('-inf')
min_answer = float('inf')
for order in permutations(order_list, N-1):
    answer = num[0]
    for c_order in range(N-1):
        if order[c_order] == 0:
            answer += num[c_order+1]
        if order[c_order] == 1:
            answer -= num[c_order+1]
        if order[c_order] == 2:
            answer *= num[c_order+1]
        if order[c_order] == 3:
            if answer < 0:
                answer = -(abs(answer)//num[c_order+1])
            else:
                answer //= num[c_order+1]
    if answer > max_answer:
        max_answer = answer
    if answer < min_answer:
        min_answer = answer

print(max_answer)
print(min_answer)