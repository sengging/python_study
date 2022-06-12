def solution(periods, payments, estimates):
    answer = [0, 0]
    old_payments = []
    new_payments = [0 for i in range(len(periods))]
    now_vip = [0 for i in range(len(periods))]
    new_vip = [0 for i in range(len(periods))]

    for x in payments:
        old_payments.append(sum(x))

    for i in range(len(periods)):
        new_payments[i] = old_payments[i] - payments[i][0]

    new_payments = [x + y for x, y in zip(new_payments, estimates)]

    for i in range(len(periods)):

        if (periods[i] >= 24) and (periods[i] < 60) and (old_payments[i] >= 900000):
            now_vip[i] += 1
        elif (periods[i] >= 60) and (old_payments[i] >= 600000):
            now_vip[i] += 1

        if (periods[i] + 1 >= 24) and (periods[i] < 60) and (new_payments[i] >= 900000):
            new_vip[i] += 1
        elif (periods[i] + 1 >= 60) and (new_payments[i] >= 600000):
            new_vip[i] += 1

    for i in range(len(new_vip)):
        if now_vip[i] < new_vip[i]:
            answer[0] += 1
        elif now_vip[i] > new_vip[i]:
            answer[1] += 1

    return answer