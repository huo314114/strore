x, y = 0, 0
while x <= 20:
    x = x + 3
    y = y + 1
    if x >= 20:
        print('青蛙出来了')
        print(y)
        break
    else:
        x = x - 2