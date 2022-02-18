# 2798
# 인덱스로 원소 제거할 때는 pop 또는 del 사용
# pop은 반환하고 del은 반환값 없음
from itertools import combinations
N, M = map(int, input().split())
card_list = list(map(int, input().split()))

best_case = list(combinations(card_list, 3))

best_num = []
for i in range(len(best_case)):
    hap = sum(best_case[i])
    best_num.append(hap)

best_num = list(set(best_num))

remove_list = []
for i in range(len(best_num)):
    if best_num[i] > M:
        remove_list.append(best_num[i])

best_num = set(best_num) - set(remove_list)
best_num = list(best_num)
best_num.sort(reverse=True)

print(best_num[0])