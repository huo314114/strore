city = {
    "北京": {
        "昌平": {
            "八达岭": ["八达岭长城"],
            "回龙观": ["永旺超市", "永辉超市", "呷哺呷哺"]
        },
        "朝阳": {
            "景观": ["玉渊潭公园"]
        },
        "海淀": {
            "高校": ["清华", "北大"],
            "公园": ["香山", "植物园"],
            "博物馆": ["军事博物馆", "国家地质公园"]
        }
    },
    "上海": {


    }
}

shop=[
    ["电脑",6000],
    ["手机",4000],
    ["耳机", 350],
    ["咖啡", 100],
    ["包子", 50],
    ["饮料", 150],
    ["平板", 5000],
]

def showCity(data):
    for d in data:
        print(d)

mycart=[]


def shopping():
    salary = input("请输入您的余额：")
    salary = int(salary)
    while True:
        chose=input("请输入您要的商品编号:")
        if chose.isdigit():
            chose = int(chose)
            if chose < len(shop):
                if salary >=shop[chose][1]:
                    mycart.append(shop[chose])
                    salary=salary-shop[chose][1]
                    print("恭喜，添加成功，您的余额还剩：￥",salary)
                else:
                    print("余额不足!")

            else:
                print("您输入有误，请再次输入!")
        elif chose=='Q'or chose=='q':
                print("欢迎下次光临，再见!")
                break


while True:
    print("*****************欢迎来到企鹅旅行社*******************")
    print("有以下城市可以去：")
    showCity(city)
    chose0=input("请输入你要去的城市：")
    if chose0=="q" or chose0=="Q":
        print("欢迎下次光临！")
        break
    else:
        showCity(city[chose0])
        chose1 = input("请输入您要去二级城市：")
        if chose1 == "q" or chose1 == "Q":
            print("欢迎下次光临！")
            break
        elif chose1 not in city[chose0]:
            print("输入错误!")

        else:
            showCity(city[chose0][chose1])
            chose2 = input("请输入要去的具体景点：")
            if chose2 == "q" or chose2 == "Q":
                print("欢迎下次光临！")
                break
            elif chose2 not in city[chose0][chose1]:
                print("没有这个景点！")
            else:
                showCity(city[chose0][chose1][chose2])
                print("每张票1000元/人！")
                chose3=input("是否买点纪念品？是或否，y或n")
                if chose3=="是" or chose3=="y":
                    for index, value in enumerate(shop):
                        print(index, value)

                    shopping()
                    print("*********购物车*********")
                    for index, value in enumerate(mycart):
                        print(index, value)

                else:
                    print("祝你旅游愉快!")