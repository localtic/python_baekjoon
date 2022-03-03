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