def solution(p):
    answer = [0 for i in range(len(p))]

    for i in range(len(p)):
        _min = p[i]

        for j in range(i, len(p)):
            if _min > p[j]:
                _min = p[j]

        a = p.index(_min)
        if i != a:
            p[i], p[a] = p[a], p[i]
            answer[i] += 1
            answer[a] += 1

    return answer

print(solution([2,5,3,1,4]))