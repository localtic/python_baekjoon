# ord("문자") 문자를 아스키 코드로 반환
# chr(num) 숫자를 아스키 코드로 반환
# 아스키코드 출력할 때 숫자인지 아닌지 판별 안 해줘도 됨

# 11654
N = input()
print(ord(N))

# 11720
N = int(input())
A = [int(i) for i in input()]
print(sum(A))

# 10809
# 알파벳 소문자 리스트 ascii_lowercase
# 알파벳 대문자 리스트 ascii_uppercase
# from에 들어가는 이름으로 파일명 지으면 그 파일이 실행됨 조심!
from string import ascii_lowercase
alpha = list(ascii_lowercase)

# list(str) 하면 string 각 글자를 리스트로 반환함
S = input()
S_list = list(S)

# str.index("a") 그 글자가 들어간 최초의 인덱스 반환
# try를 시도하는데 에러가 나면 except 구문 실행
result = []
for i in alpha:
    try:
        a = S_list.index(i)
        result.append(str(a))
    
    except:
        result.append("-1")

#join은 list의 요소가 str이어야 함, int 안 됨
print(" ".join(result))


# 2675
# end가 input의 공백도 없애버리는 걸 조심
T = int(input())

for i in range(T):
    R, A, *B = input()
    R = int(R)
    for k in range(len(B)):
        print(B[k] * R, end="")
    print()


# 1157
from collections import Counter

word = input()
word = word.upper()

word_list = list(word)
cnt = Counter(word_list)
most_cnt = dict(cnt.most_common(2))

key_list = list(most_cnt.keys())
value_list = list(most_cnt.values())

# not value_list 아무것도 입력하지 않았을 경우(빈 리스트) 처리 안 해줘도 정답 처리
if not value_list or len(value_list) >= 2 and value_list[0] == value_list[1]:
    print("?")

else:
    print(key_list[0])


# 1152
# 공백만 입력할 경우를 생각하자
# not S 빈 문자열인 경우
S = input().strip()
cnt = S.count(" ")

if not S:
    print(0)
else:
    print(cnt+1)


# 2908
A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)


# 5622
# 숫자 1 -> 2초
# 따라서 해당 알파벳 숫자 + 1초 만큼걸림
# WA -> W + A -> (9 + 1) + (2 + 1)
phone_number = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9
} 

# 사전 = {"가": 10, "나": 100}
# 사전["가"]
# values()는 값 리스트 반환

word = input()
time = 0
# 각 알파벳에 해당하는 값 + 1을 누적한다.
# ex) UNIC -> U + N + I + C -> (8 + 1) + (6 + 1) + (4 + 1) + (2 + 1)
# for i in range(len(word))는 i에 숫자로 들어감
for i in word:
    for k in phone_number.keys():
        if i in k:
            time += phone_number[k] + 1
            break
print(time)


# 2941
# replace는 다시 바인딩 필요
cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in cro_list:
    if i in word:
        word = word.replace(i, "*")
print(len(word))


# 1316
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)