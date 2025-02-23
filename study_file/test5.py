#BMI = 体重 / (身高 ** 2)
user_weight = float(input("请输入您的体重（单位：kg）："))
user_hight = float(input("请输入您的身高（单位：m）："))
while user_weight != "q":
    user_weight = float(input("请输入您的体重（单位：kg）："))
    user_hight = float(input("请输入您的身高（单位：m）："))
    user_BMI = user_weight/(user_hight) ** 2
    print("您的BMI值为："+ str(user_BMI))

#偏瘦：user_BMI <= 18.5
#正常：18.6 < user_BMi <= 25
#偏胖：25 < user_BMI <= 30
#肥胖： user_BMI > 30

    if user_BMI <= 18.5:
        print("你属于偏瘦")
    elif 18.5 < user_BMI <= 25:
        print("'你属于正常")
    elif 25 < user_BMI <= 30:
        print("你属于偏胖")
    elif 30 < user_BMI:
        print("你属于肥胖")