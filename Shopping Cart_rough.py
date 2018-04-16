"""
title：python实现购物车列表并购买
purpose：简单地python逻辑复习，以及基础回顾，无聊闲的
author：Zisc

"""

goods =[
    {"name":"电脑","price":5399},
    {"name":"电视","price":3000},
    {"name":"电动车","price":2399},
    {"name":"手机","price":2999},
    {"name":"洗衣机","price":3399},
]
shoc={"购物车":[]}
money = input("请输入你的银两：")
for key,item in enumerate(goods,1):
    print(key,item)
flag = 1
sum = 0
print("附带命令模式1:查看当前购物车insept,2:结算exit")
while flag :
    ret = input("请输入加入购物车的商品序号：")
    if ret.isdigit()and int(ret)<=5:
        num = int(ret)-1
        shoc["购物车"].append(goods[num])

    elif ret =="insept":
        print("当前购物车：",shoc["购物车"])
    elif ret == "exit":
        flag=0

for i in shoc["购物车"]:
    sum =sum + i["price"]
print("购物车结算的总价格为%d"%sum)
if int(money)>=sum:
    balance = int(money)-sum
    print("购买成功还剩余额：%d"%balance)
else:
    print("余额不足")
