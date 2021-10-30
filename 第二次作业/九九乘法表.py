i=1
while i<10:
    j=1
    while j<=i:
        print("%dx%d=%-2d "%(j,i,i*j),end='')
        j+=1
    print("")
    i+=1