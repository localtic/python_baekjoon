n = int(input())
guest = list(map(int, input().split()))

old = []
cnt = 0
for i in range(n):
    if guest[i] in old:
        cnt += 1
    else:
        old.append(guest[i])
print(cnt)