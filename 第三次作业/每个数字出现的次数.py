
List =[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a=set(List)
print(List)
print(a)
for i in a:
    count =List.count(i)
    print(i,'出现的次数：',count)