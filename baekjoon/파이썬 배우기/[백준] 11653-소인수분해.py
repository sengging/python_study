N = int(input())
_list = []
if N == 1:
    print('')
else:
    while (N!=1):
        for i in range(2,int(N)+1):
            if N%i == 0:
                _list.append(i)
                N = N/i
                break
    _list.sort()
    for x in _list:
        print(x)