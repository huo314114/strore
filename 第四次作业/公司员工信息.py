# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
age = ['姓名','年龄', '性别', '编号', '任职公司', '薪资', '部门编号']
emintion = {}
s = 0
while s < len(names):
    i = 1
    a = {}
    while i <= 6:
        a[age[i]] = names[s][i]
        i += 1
    emintion[names[s][0]] = a
    s += 1
print(emintion)
age1 = ['年龄', '性别', '编号', '任职公司', '薪资', '部门编号']
for tal in names:
    emintion[tal[0]] = {age1[x]:tal[1:][x] for x in range(len(age1))}
print(emintion)