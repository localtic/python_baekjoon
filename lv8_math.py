# 1712
# 시간 복잡도를 고려하자
# 시간이 짧으면 한 번의 계산에서 끝낼 수 있도록 
# 상수만큼의 반복문은 괜찮지만 이외의 반복문 자제
# 파이썬 보통 초당 연산 2천만번 수행
# 21억 조건 있으면 이런 거 무조건 들어옴
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A // (C-B) + 1)


# 2292
# 시그마 1부터 N까지의 합 N(N+1)/2
room = int(input())

i = 0
while True:
    if room > 1 + 6 * i * (i+1) // 2:
        i += 1
    else:
        print(i+1)
        break


#2839
N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)


# 2869
# math.ceil() 올림
import math
A, B, V = map(int, input().split())
D = (V-B) / (A-B)
D = math.ceil(D)
print(D)


# 10757
A, B = map(int, input().split())
print(A+B)