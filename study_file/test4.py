mood_index = int(input("女朋友今天的心情指数："))
at_home =str(input("女朋友是否在家："))
if mood_index < 60:
    if at_home == "yes":
        print("不能玩游戏")
    elif at_home == "no":
        print("可以玩游戏")
else:
    print("可以玩游戏")


