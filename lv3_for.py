# 구구단
N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} =", N*i)

# A+B
T = int(input())
for _ in range(1, T+1):
    A, B = map(int, input().split())
    print(A+B)
# _ 의미 없는 Iterator 사용할 때, 횟수대로 반복만 함

n = int(input())
for i in range(1, n+1):
    i += 1
print(i)

# sys, 합 구하기
import sys
n = int(sys.stdin.readline())
hap = 0
for i in range(1, n+1):
    hap += i
print(hap)

n = int(input())
hap = 0
for i in range(1, n+1):
    hap += i
print(hap)

print(sum(list(range(1, int(input()) + 1))))

# 빠른 합 구하기 
import sys
T = int(sys.stdin.readline())
for _ in range(1, T+1):
    A, B= map(int, sys.stdin.readline().split())
    print(A + B)

# 한 줄에 하나씩 출력
N = int(sys.stdin.readline())
for i in range(1, N+1):
    print(i);

# 한 줄에 하나씩 거꾸로
N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    print(i);

# 숫자 증가, 합
T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}:", A+B)

# 합 마지막
T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")

# 별 출력
N = int(sys.stdin.readline())
for i in range(1, N+1):
    print("*"*i);

# 정렬된 별
import sys
N = int(sys.stdin.readline())
for i in range(1, N+1):
    print(" "*(N-i)+"*"*i);

# 트리
import sys
N = int(sys.stdin.readline())
print("        ", N)
for i in range(1, N+1):
    print(" "*(N-i)+"*"*i+"*"*i+" "*(N-i));

# end를 잊지 말자
import sys
N, X = map(int, sys.stdin.readline().split())
A = map(int, sys.stdin.readline().split())
for i in A:
    if(i < X):
        print(i, end=' ')