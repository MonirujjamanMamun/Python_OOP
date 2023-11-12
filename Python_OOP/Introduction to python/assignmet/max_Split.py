
S = input()

R_count = 0
L_count = 0
ans = []

for char in S:
    if char == 'R':
        R_count = R_count + 1
    else:
        L_count = L_count + 1
    if R_count == L_count:
        ans.append(S[:R_count + L_count])
        S = S[R_count + L_count:]
        R_count = 0
        L_count = 0

print(len(ans))
for s in ans:
    print(s)
