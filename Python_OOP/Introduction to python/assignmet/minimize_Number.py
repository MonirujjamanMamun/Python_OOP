

N = int(input())
A = list(map(int, input().split()))


max_count = 0
while True:
    tiger = 1
    for i in range(N):
        if A[i] % 2 != 0:
            tiger = 0
            break
    if tiger:
        max_count += 1
        for i in range(N):
            A[i] //= 2
    else:
        break


print(max_count)
