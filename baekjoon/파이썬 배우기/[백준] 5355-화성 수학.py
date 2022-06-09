T = int(input())
for i in range(T):
    _list = list(map(str,input().split()))
    _list[0] = float(_list[0])
    for x in _list:
        if x == '#':
            _list[0]-=7
        elif x == '%':
            _list[0]+=5
        elif x == '@':
            _list[0]*=3
    print(f"{_list[0]:.2f}")



