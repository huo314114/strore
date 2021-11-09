Friuts = {
    '苹果': 12.3,
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8}

# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# print(Friuts.get(input('请输入要查询的水果名'), '没有此水果'))
# 请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 1
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 1
    }
}

d = 0
Friuts_money = list(Friuts.values())
for name_ in info.keys():
    c = 0
    for a in Friuts.keys():
        b = info[name_]['fruits'].get(a, -1)
        if b == -1:
            continue
        else:
            c = c + b * Friuts_money[d]
            d += 1
    info[name_]['money'] = c
print(info)