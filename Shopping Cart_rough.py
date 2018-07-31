"""
title：python实现购物车列表并购买
purpose：简单地python逻辑复习，以及基础回顾，无聊闲的
author：Zisc

"""

"""
1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

--------------------------------------------------------------------------------------------------------
1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
2、允许查询之前的消费记录
---------------------------------------------------------------------------------------------------------
    我用到了3个文件操作，分别是:
    1.记录账号密码的文件（用于验证）----> user_data.txt，默认存放用户的用户名及密码
    2.用于记录用户时候存在过购买的痕迹 -----> lock_user.txt(先默认不创建),有成功购买记录后则会用户被记录
    3.账号在商场的购买记录---------> xxx_purchase_record.txt(先默认不创建)，每个账号分别单独保存
    我都尽量做了注释，可能有的地方我没能解释很清楚，望老师谅解，不过基本功能是实现了，唯一遗憾是（我还是不加那个增删购物车的操作啦，_(:3」∠❀)_）
    
"""
import json
from datetime import datetime


def login(username, password):
    """
    判断用户登陆是否正确登录
    :param username:
    :param password:
    :return:
    """
    with open("user_data.txt", 'r', encoding="utf-8") as f:
        u_p = [i.strip() for i in f.readlines()]
        user = str(username) + ':' + str(password)
        if user in u_p:
            return True


def has_login(username):
    """
    判断用户是否有过购买记录,记录在内的用户说明有购买记录
    :param username:
    :return:
    """
    with open("lock_user.txt", 'a+', encoding="utf-8") as f:  # 用a+ 增加通用性，因为一开始文件并不存在，用户第一次成功购买才会创建
        f.seek(0)  # 如果文章有内容指针默认会放在末尾，在进行判断的时候把他手动放回前面，不然读出来的文件是空值
        user = [i.strip() for i in f.readlines()]
        if username in user:
            return True


def main_function():
    goods = [
        {"name": "电脑", "price": 5399},
        {"name": "电视", "price": 3000},
        {"name": "电动车", "price": 2399},
        {"name": "手机", "price": 2999},
        {"name": "洗衣机", "price": 3399},
    ]
    shop_list = {"购物车": []}  # 空购物车
    if login(user_name, pass_word):  # 先判断用户是否正确输入用户名密码
        print("welcome %s Let's shopping" % user_name)  # 欢迎用户
        if has_login(user_name):  # 判断这个用户是否有购买记录，如果有购买记录，则打开他的用户记录
            with open('{}_purchase_record.txt'.format(user_name), 'r', encoding='utf-8') as f:  # 以读模式打开记录文件)
                a = [i.strip() for i in f.readlines()]  # 如果文件存在格式化每一行，
                p = json.loads(a[-1])  # 因为我在下面保存购买记录的时候是用json 把字典写进去的，这样方便调用。
                money = p['余额']  # 取出余额，并用这个余额继续购买
                print('\033[1;31m 当前余额剩下%d \033[0m' % money)
        else:  # 没有购买记录，输入金钱呗
            while True:  # 用户需要正确输入工资，输入其他则会报错
                money = input("请输入你的金钱:")
                if money.isdigit():
                    money = int(money)
                    break
                else:
                    print("\033[1;31m用户非法输入\033[0m")
                    continue
        for key, item in enumerate(goods, 1):  # 打印商品
            print(key, item)
        flag = 1  # 标志位
        shop_prices = 0  # 当前购物车价格，用于最后计算购物车所以商品的价格
        while flag:  # 用户操作
            ret = input("\033[1;31m 请输入加入购物车的商品序号(查看购物车:check,结算:exit,查看当前金钱:b,查看历史购买记录:history,充值:add) :\033[0m")
            if ret.isdigit() and int(ret) <= len(goods):  # 用户输入对应商品序号，把商品添加到购物车
                num = int(ret) - 1
                shop_list["购物车"].append(goods[num])
                print("\033[1;35m 商品>>{}已加入购物车 \033[0m".format(goods[num]))
            elif ret == "check":  # 查询购物车操作
                print("\033[1;35m 当前购物车：{} \033[0m".format(shop_list["购物车"]))
            elif ret == "exit":  # 结算，结算用户操作
                flag = 0
            elif ret == "b":  # 查看当前金钱，主要用于二次购买的时候上次购买结算后的余额
                print("\033[1;31m 当前金钱：%d \033[0m" % money)
            elif ret == 'history':  # 查询历史购买记录
                if has_login(user_name):
                    with open('{}_purchase_record.txt'.format(user_name), 'r', encoding='utf-8') as f:
                        a = f.read()
                        print("\033[1;33m{}\033[0m".format(a))
                else:
                    print("\033[1;33m无历史购买记录\033[0m")
            elif ret == 'add':  # 充值
                add_money = input('请输入要充值多少:')
                if add_money.isdigit():
                    money += int(add_money)
                    print("\033[1;31m 当前金钱：%d \033[0m" % money)
                else:
                    print("充值失败")
            else:
                print("操作有误，请输入正确指令")
        for i in shop_list["购物车"]:  # 结算操作
            shop_prices = shop_prices + i["price"]  # 算出购物车所有商品总价格
        print(" \033[1;33m购物车结算的总价格为%d \033[0m" % shop_prices)  # 打印所有物品总价格
        if money >= shop_prices:  # 购买成功则往下执行
            print("\033[1;34m 购买的物品如下 \033[0m")  # 提示购买的商品(横栏)
            for good in shop_list["购物车"]:  # 打印结算购物车的商品
                print("\033[1;35m{}\033[0m".format(good))
            balance = money - shop_prices  # 算出余额
            print("\033[1;31m购买成功还剩余额：%d \033[0m" % balance)  # 打印结算成功后所剩的余额

            # 这里是第一次对lock_user写入操作的地方，如果是用户第一次购买则打开文件然后记录。
            with open("lock_user.txt", 'a+', encoding='utf-8') as f:
                f.seek(0)
                lock_user = [i.strip() for i in f.readlines()]
                if user_name not in lock_user:  # 如果这个用户是第一次登录购买，则把他添加上这个文件，下次登录的时候就不用再输入金钱，直接用余额购买
                    f.write('{}\n'.format(user_name))

            # 购买记录文件,如果是第一次登录则创建并添加这次的购买记录，如果不是头一次则把记录往后添加呗
            with open("{}_purchase_record.txt".format(user_name), 'a+', encoding='utf-8') as f:
                shop_record = dict()
                shop_record['余额'] = balance
                shop_record['购买时间'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                shop_record['购物车'] = shop_list["购物车"]
                shop_record['本次消费'] = shop_prices
                f.write("{}\n".format(json.dumps(shop_record, ensure_ascii=False)))  # 序列化后写入文件
        else:  # 余额不足，购买失败
            print("\033[1;33m余额不足\033[0m")
    else:
        print("用户验证失败，请输入正确的账号及密码")


if __name__ == '__main__':
    user_name = input("请输入你的账号:")
    pass_word = input("请输入你的密码:")
    main_function()
