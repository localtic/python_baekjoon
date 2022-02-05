# 입력받은 str을 split() 해야 리스트 됨
# map 하고 list 붙이는 거 잊지 말자
import sys
A = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
print(min(N), max(N), end=" ")

# append는 반환값이 없다! 계속 리스트에 저장됨
# .strip()은 readline()으로 입력받을 때 줄바꿈을 제거
# range(1, 10) = range(9)
# max()는 for문에 넣지 말고 변수에 값을 넣어 비교하자
import sys
list1 = []
for i in range(9):
    list1.append(sys.stdin.readline().rstrip())

list1 = list(map(int, list1))
max_num = max(list1)

for i in range(0, len(list1)):
    if list1[i] == max_num:
        max_idx = i + 1

print(max(list1))
print(max_idx)

# 곱하기 결과값 숫자의 개수
# sort(), append()는 반환값이 없는 함수임
from collections import Counter
A = int(input())
B = int(input())
C = int(input())

total = str(A * B * C)
cnt = dict(Counter(total))

for i in range(10):
    if str(i) in cnt:
        pass
    else:
        cnt[str(i)] = 0

cnt = sorted(cnt.items())
cnt = dict(cnt)
cnt = list(cnt.values())
for i in cnt:
    print(i)

# 나머지의 개수
# set 타입으로 list의 중복값을 제거할 수 있다
list1 = []
for i in range(10):
    A = int(input())
    list1.append(A % 42)
list1 = list(set(list1))
print(len(list1))

# 새로운 평균 구하기
import sys
N = int(sys.stdin.readline())
grade_list = list(map(int, sys.stdin.readline().split()))
max_grade = max(grade_list)

result = []
for i in range(N):
    A = grade_list[i]/max_grade*100
    result.append(A)
print(sum(result)/N)
