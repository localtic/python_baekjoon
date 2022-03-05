# 2750
N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)

# 2751
import sys
N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for i in numbers:
    print(i)


# 10989
import sys
from collections import defaultdict

N = int(input())
numbers = defaultdict(int)

for i in range(N):
    number = int(sys.stdin.readline())
    numbers[number] += 1

numbers_keys = sorted(numbers.keys())

# 정렬된 키를 사용하기 때문에 딕셔너리는 다시 정렬하지 않아도 됨
for key in numbers_keys:
    for _ in range(numbers[key]):
        print(key)

# 존재하지 않는 key가 들어왔을 때 그 타입의 default value로 값 지정되고 그 키가 생김
# defaultdict(int) value에 0
# defaultdict(list) value에 빈 리스트

# defaultdict가 없었다면
if number not in numbers:
    numbers[number] = 1
else:
    numbers[number] += 1

# dict.items() 튜플로 된 리스트, dict.keys(), dict.values()    
# alphabet = {"A": 1, "B": 2, "C": [2, 3, 7]}
# alphabet.keys() == ["A", "B", "C"]
# alphabet.values() == [1, 2, [2, 3, 7]]
# alphabet.items() == [("A", 1), ("B", 2), ("C", [2, 3, 7])]