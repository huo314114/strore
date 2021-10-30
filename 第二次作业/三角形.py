'''
def new_func(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if a + b > c:
        if b + c>a:
            if a+c>b:
                print("能组成三角形")
            else:
                print("不能组成三角形")
        else:
            print("不能组成三角形")
    else:
        print("不能组成三角形")
    if a== b or b==c or a==c:
        print("这个三角形是等边三角形")
    a =a**2
    b =b**2
    c =c**2
    if  a + b==c or c+b==a or a+c==b:
        print("这个三角形是直角三角形")
d=int(input())
e=int(input())
f=int(input())
new_func(d,e,f)
'''


c, d = 0, [0, 0, 0]
while c < 3:
    d[c] = int(input('请输入第%s条边' % (c + 1)))
    c = c + 1
if d[0] <= 0 or d[1] <= 0 or d[2] <= 0:
    print('不能形成三角形')
elif d[0] + d[1] <= d[2] or d[0] + d[2] <= d[1] or d[2] + d[1] <= d[0]:
    print('不能形成三角形')
elif d[0] == d[1] == d[2]:
    print('形成等边三角形')
elif d[0] == d[1] or d[1] == d[2] or d[0] == d[2]:
    print('形成等腰三角形')
elif d[0] ^ 2 + d[1] ^ 2 == d[2] ^ 2 or d[0] ^ 2 + d[2] ^ 2 == d[2] ^ 2 or d[2] ^ 2 + d[1] ^ 2 == d[0] ^ 2:
    print('形成直角三角形')
else:
    print('形成普通三角形')

