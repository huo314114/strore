import random
bank_name = "中国农业银行昌平沙河支付行"
bank = {}


# 展示各项业务
def welcome():
    print("*****************************")
    print("*    中国农业银行账户管理系统    *")
    print("*****************************")
    print("*           选项             *")
    print("*          1.开户            *")
    print("*          2.存钱            *")
    print("*          3.取钱            *")
    print("*          4.转账            *")
    print("*          5.查询            *")
    print("*          6.Bye!           *")
    print("*****************************")


# 开户方法
def bank_root(account_type,names,password,country,province,street,door,remaining_sum):
    # 判断银行库是否已满
    if len(bank) > 100:
        return 3
    if names in bank:
        return 2
    bank[names] = {
        "account_type":account_type,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "remaining_sum":remaining_sum,
        "bank_name":bank_name
    }
    return 1


# 取钱
def drawmoney():
    account_number = input("请输入您的账号:")
    password = input("请输入您的密码:")
    drawmoney = input("请输入您的取钱金额:")



# 取钱方法
def bank_drawmoney():
    account_number=input("请输入您的姓名:")
    if account_number not in bank:
        return (1,0)
    elif account_number in bank:
        password = input("请输入您的密码:")
        if password != bank[account_number]['password']:
            return (2,0)
        else:
            money=int(input('请输入您要取的金额'))
            if money > bank[account_number]['remaining_sum']:
                return (3,0)
            else:
                bank[account_number]['remaining_sum']-=money
                return (4,bank[account_number]['remaining_sum'])


def drawmoney_1():
    (c,d)=bank_drawmoney()
    if c==1:
        print('请您先开户:')
    elif c==2:
        print("密码错误!")
    elif c==3:
        print("余额不足!")
    elif c==4:
        print("取款成功!")
        print("您的余额为",d)





# 开户
def root():
    names = input("请输入您的姓名:")
    account_type = input("请输入您的账户类型:")
    password = input("请输入您的密码:")
    country = input("请输入您的国籍:")
    province = input("请输入您的省份:")
    street = input("请输入您的街道:")
    door = input("请输入您的门牌号:")
    remaining_sum = int(input("请输入您的存款余额:"))

    account_number = random.randint(10000000,99999999)

    # 调用信息
    status = bank_root(account_type,names,password,country,province,street,door,remaining_sum)

    if status ==3:
        print("银行库已满!")
    elif status == 2:
        print("不能重复开户!")
    elif status == 1:
        print("开户成功!")
        into ='''
            ***********个人信息***********
            用户名:%s
            账号:%s
            账户类型:%s
            取款密码:%s
            地址信息:
                国籍:%s
                省份:%s
                街道:%s
                门牌号:%s
            存款余额:%s
            开户行名称:%s
        '''
        print(into % (names,account_number,account_type,password,country,province,street,door,remaining_sum,bank_name))




while True:
    welcome()
    chose =input("请输入业务编号:")

    if chose == "1":
        root()
    elif chose == "2":
        pass
    elif chose == "3":
        drawmoney_1()
    elif chose == "4":
        pass
    elif chose == "5":
        pass
    elif chose == "6":
        break
    else:
        print("输入错误!请重新输入!")









