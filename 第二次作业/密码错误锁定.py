name='root'
passwd='admin'
for i in range(0,3):
    usr_name=input("用户名:")
    usr_passwd=input("密码:")
    if usr_name ==name and usr_passwd==passwd:
        print("ok")
        break
    elif name !=usr_name or passwd !=usr_passwd:
        if i <2:
            i += 1
            print("用户名密码错误,请重新输入!")
        else:
            print("您的账号已被锁定")
