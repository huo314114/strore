# 编写一个函数，传入一个列表，并统计每个数字出现的次数，返回字典数据。
a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8]
def countnum(a):
    sep = list(set(a))
    dict1 = dict.fromkeys(sep, 0)
    x = 0
    while x < len(sep):
        dict1[sep[x]] = a.count(sep[x])
        x = x + 1
    return dict1
def countnums(a):
    dict1 = {}
    for i in a:
        if str(i) not in dict1.keys():
            dict1[str(i)] = 1
        else:
            dict1[str(i)] += 1
    return dict1
dict1 = countnums(a)
dict2 = countnum(a)
print(dict1,dict2)