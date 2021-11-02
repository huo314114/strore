a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(len(a)-1):
    for j in range(1,len(a)-i):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
print(a)