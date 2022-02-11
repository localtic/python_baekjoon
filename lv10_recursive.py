N = int(input())

def fact(N):
    if N == 1 or N == 0:
        return 1
    
    return N * fact(N-1)

print(fact(N))

# 넘겨주거나
# 밖에 있는 걸 쓰거나