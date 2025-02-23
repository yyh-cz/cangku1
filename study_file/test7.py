tongxunlu_dict = {"杨译涵":"13203605121",
                  ("姜颖",1):"17732179857",
                  ("姜颖",2):"19933129280"}
tongxunlu_dict["李臻"] = "1327355468"

name = input("请输入你要找的人名：")
if name in tongxunlu_dict:
    print(name + "的号码如下：")
    print(tongxunlu_dict[name])
else:
    print("您所查找的名字不在通讯录")
    print("通讯录总共记录号码数：" + str(len(tongxunlu_dict)))