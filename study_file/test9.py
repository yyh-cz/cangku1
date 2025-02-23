print("你好，我是一个求得平均值的计算器")
total = 0
count = 0
user_input = input("请输入数字（完成所有数字输入后，请输入q来得到结果）：")
while user_input != "q":
    num = float(user_input)
    total += num   #这个也可以写为 total = total + num
    count = count + 1 #这个也可以写为 count += 1
    user_input = input("请输入数字（完成所有数字输入后，请输入q来得到结果）：")
if count == 0:
    result = 0
else:
    result = total / count
print("你输入数字平均值为" + str(result))