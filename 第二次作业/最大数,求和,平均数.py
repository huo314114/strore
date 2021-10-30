a,num,num_max,num_sum=0,0,0,0
while a<10:
    a+=1
    num=int(input("请输入第%s数字"%a))
    if num>num_max:
        num_max=num
    num_sum=num_sum+num

print(num_max)
print(num_sum)
print("%.2f"%(num_sum/10))