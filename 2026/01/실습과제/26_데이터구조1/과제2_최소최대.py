# 아래 함수를 수정하시오.

# def find_min_max(lis):
#     lis.sort()
#     return lis[0], lis[-1]

def find_min_max(lis):
    return min(lis), max(lis)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)