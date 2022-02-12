# 매개변수를 적는 것도 변수를 선언하는 것
# 매개변수와 외부 변수의 이름을 같게 하지 말자!
num = int(input())

def fact(N):
    if N == 1 or N == 0:
        return 1
    
    return N * fact(N - 1)

print(fact(num))

# 매개변수로 넘겨주거나
# 밖에 있는 변수값을 사용

a = 100
b = 100
def add(x, y):
    return x + y

def global_add(x, y):
    return a + b

print(add(50, 100))
print(global_add(50, 100))

# 변수의 스코프!
# 변수 찾는 위치 지역 -> 전역
# 한 단계 위의 범위에서 찾는다