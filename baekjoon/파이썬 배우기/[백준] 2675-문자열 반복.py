T = int(input())
for i in range(T):
    R, S = list(map(str,input().split()))
    R = int(R)
    new=''
    for x in S:
        new+=x*R
    print(new)

