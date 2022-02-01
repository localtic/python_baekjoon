# \\ 두 번 해야 역슬래시 출력됨
# 아니면 escape

print("\n 고양이")
print("\    /\\");
print(" )  ( ')");
print("(  /  )");
print(" \(__)|")

print("\n강아지")
print("|\\_/|");
print("|q p|   /}");
print('( 0 )"""\\');
print('|"^"`    |');
print("||_/=\\__|")

print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

# input()은 문자열로 받음
# 문자열을 split()
# split()은 공백이 default
# A, B = map(int, input().split())
# print(A + B)

A, B = map(int, input().split())
print(A-B)

A, B = map(int, input().split())
print(A*B)

A, B = map(int, input().split())
print(A/B)

# / 하나면 다 나누기
# // 하면 몫만
# A, B = map(int, input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

# 변수명으로 뭘 해도 그 변수에 input이 들어감
# joonas = input()
# print(joonas +"??!")

# y = int(input())
# print(y - 543)

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

A = int(input())
B = input()
C = [B[0], B[1], B[2]]
C = list(map(int, C))
print(C[2] * A)
print(C[1] * A)
print(C[0] * A)
print(A * int(B))

for i in C:  
    print(C[-i] * A)
print(A * int(B))

# for i in C 하면 C의 요소가 들어감
# index가 아니라...