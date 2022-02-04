# for문 = 반복해야 할 횟수를 알 때 사용
# while문 = 반복해야 할 횟수 모르지만, 종료 조건을 알 때 사용

# input 0, 0일 때 종료
import sys
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A==0 and B==0:
        break
    print(A+B)

import sys
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A==0 and B==0:
        break
    print(A+B)

# 입력이 없으면 종료함
# i, readlines() 사용으로 총 입력 개수 알아냄
import sys
lines = sys.stdin.readlines()
for i in lines:
    A, B = map(int, i.split())
    print(A+B)

# End of File을 알아내는 방법
# try~except로 오류 발생 시 빠져나오도록
# 입력이 없으면 종료됨
import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break

