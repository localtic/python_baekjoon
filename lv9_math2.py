# 1978
# 제곱근 구하기
# 지수승 **
# 2 ** 0.5 = 루트2

# 소수 판별하는 법
# 나머지가 0인 건 1과 자기자신뿐
# 2부터 루트 자기 자신까지

# 변수, 함수 이름만 보고 유추 가능해야 함
N= int(input())
numbers = list(map(int, input().split()))

if 1 in numbers:
    numbers.remove(1)

numbers_duplicate = numbers.copy()

for number in numbers:
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            numbers_duplicate.remove(number)
            break
        
print(len(numbers_duplicate))
    
# cnt = 0
# def is_prime(n):
#     for i in range(2, n**0.5):
#         if n % i == 0:
#             return


# 2581
# 소수에서 1을 생각하자!!
M = int(input())
N = int(input())

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def get_prime_list(start, end):
    prime_list = []
    for k in range(start, end+1):
        if is_prime(k):
            prime_list.append(k)
    return prime_list

prime_list = get_prime_list(M, N)

if not prime_list:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))


# 11653
# 소인수분해
N = int(input())

factor = 2

while factor <= N:
    if N % factor == 0:
        print(factor)
        N //= factor
    else:
        factor += 1

# 소수가 필요하지 않았는데 바보 같은 짓을 했다

N = int(input())
if N == 1:
    exit()
    
# 소인수분해 = 숫자를 소수들의 곱으로 나타내는 것
# 주어진 수가 소수인지 판별하는 함수

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

# N/2 이하의 수 중에서 소수 담긴 리스트 만들어주는 함수
# 전역변수는 외부 영향을 받을 수 있으니 함수 내부에서 사용할 거면 내부에서 변수 만들기
# 협업 시 주의
def get_prime_list(number):
    prime_list = []
    for k in range(2, number//2+1):
        if is_prime(k):
            prime_list.append(k)
    return prime_list

# for문으로 N을 소수 리스트에서 하나씩 나누는데
# 함수를 호출하면 return 값으로 대체, return값 없으면 None 반환
prime_list = get_prime_list(N)

for prime in prime_list:
    while N % prime == 0:
        print(prime)
        N = N // prime
        if N % prime != 0:
            break

# 4153 직각삼각형
while True:
    triangle = list(map(int, input().split()))
    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break
    c = max(triangle)
    triangle.remove(c)
    
    if triangle[0] ** 2 + triangle[1] ** 2 == c ** 2:
        print("right")      
    else:
        print("wrong")


# 4948
def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def get_prime_list(start, end):
    prime_list = []
    for k in range(start+1, end+1):
        if is_prime(k):
            prime_list.append(k)
    return prime_list

# 순서를 잘 보고 필요하지 않은 값을 출력하지 않도록 하자
while True:
    N = int(input())
    if N == 0:
        break
    prime_list = get_prime_list(N, 2*N)
    print(len(prime_list))