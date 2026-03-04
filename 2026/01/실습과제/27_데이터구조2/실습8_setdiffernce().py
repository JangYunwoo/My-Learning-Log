def ordered_difference_sets(set1, set2):
    result = [set1.difference(set2), set2.difference(set1)]
    if set() in result:
        result.sort(key=lambda x: len(x))
    return result[0], result[1]

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
