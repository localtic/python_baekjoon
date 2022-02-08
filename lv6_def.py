# 함수 작성하는 문제는 함수만 작성하면 됨!
# 인풋값에 작업 안 해줘도 됨
def solve(a):
    return sum(a)

N = int(input())

# 15596
# FIFO, LIFO
# fact()에 결과값이 들어감
# 재귀함수는 종료 조건이 중요함
def fact(N):
    if N == 1:
        return 1
    else:
        return N * fact(N-1)
fact(N)


# 4673
# set() = set 선언하는 방법
# list의 append = set의 add
numbers = set()
def d(N):
    numbers.add(N + sum([int(i) for i in str(N)]))
    
for i in range(1, 10001):
    d(i)

for i in range(1, 10001):
    if i not in numbers:
        print(i)


# 1065 - 1
def han(N):
    cnt = 0
    for i in range(1, N+1):
        list1 = list(map(int, str(i)))
        if i < 100:
            cnt += 1

        elif list1[0] - list1[1] == list1[1] - list1[2]:
            cnt += 1
    return cnt
print(han(int(input())))

# 1065 - 2
# 매개변수로 받는 것을 권장
# 하나의 함수 하나의 기능만

# 코드를 한 줄로 쭉 적는다고 좋은 코드는 아님
# 가독성이 좋은 코드를 만들자
N = int(input())

def han(num):
    cnt = 0
    for i in range(1, num+1):
        if i < 100:
            cnt += 1
        elif 100 <= i < 1000:
            i = str(i)
            if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
                cnt += 1
    return cnt

print(han(N))

# 노가다를 줄여보자
i = str(i)
int(i[0]) - int(i[1]) == int(i[1]) - int(i[2])


list = [int(k) for k in str(i)]
list[0] - list[1] == list[1] - list[2]