r=int(input("请输入您要打印的三角形的层数"))
while r>0:
    for i in range(1,r+1):
        print(' '*r,'* '*i)
        r-=1