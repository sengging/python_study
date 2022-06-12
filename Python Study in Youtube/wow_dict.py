fruits = ['사과', '사과', '바나나', '바나나', '딸기', '키위', '복숭아', '복숭아', '복숭아']
dic = {}
for fruit in fruits:
    if fruit in dic:
        dic[fruit] = dic[fruit] + 1
    else:
        dic[fruit] = 1

print(dic)
