A, B= map(int, input().split())
if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")
# 여러 개 받으면 split 해야 함
# split()은 string을 잘라서 list를 만든다

def add_1(x):
    return x + 1

list1 = [0, 1, 2, 8, 9, 3]
list2 = list(map(add_1, list1))
print(list2)

A = int(input())
if(90 <= A <= 100):
    print("A")
elif(A<=89) and (A>=80):
    print("B")
elif(A<=79) and (A>=70):
    print("C")
elif(A<=69) and (A>=60):
    print("D")
else:
    print("F")
# input은 string으로 들어가는 거 주의


x = int(input())
y = int(input())

if(x>0) and (y>0):
    print("1")
elif(x<0) and (y>0):
    print("2")
elif(x<0) and (y<0):
    print("3")
else:
    print("4")

H, M = map(int, input().split())
if(45<=M<=59):
    print(H, M-45)
elif(0<=M<45) and (1<=H<=24):
    print(H-1, M+15)
elif(0<=M<45) and (H==0):
    print(23, M+15)
# else:
#     pass

import sys
sys.stdin.readline()
# stdin 스탠다드 인풋
# readline() 한 줄을 읽겠다

# 2525
# 시간을 24로 나누기
# 분을 60으로 나누기
from sys import stdin
stdin.readline()

hour, min = map(int, input().split())
times = int(input())

minute = min + times
print((hour+minute // 60) % 24, minute % 60)


# 2480
A, B, C = map(int, input().split())
list = [A, B, C]

if A == B == C:
    print(10000+A*1000)
elif A == B != C or A == C != B:
    print(1000+A*100)
elif A != B == C:
    print(1000+B*100)
else:
    print(max(list) * 100)