e1 = 0
mogic = [['罗恩', 23, 35, 44],
         ['哈利', 60, 77, 68, 88, 90],
         ['赫敏', 97, 99, 89, 91, 95, 90],
         ['马尔福 ', 100, 85, 90]]
while e1 < len(mogic):
    e2, e3 = 0, 0
    while e2 < len(mogic[e1]):
        if e2 < 1:
            print(mogic[e1][e2], end=':')
        else:
            e3 = e3 + mogic[e1][e2]
        e2 += 1
    print(e3)
    e1 += 1