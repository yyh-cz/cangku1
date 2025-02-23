print("这是一个算术平均值计算器")
count = 0
total = 0
user_input = input("请输入一个数字，按q进行结束并输出结果:")
while user_input != "q":
    count += 1
    num = float(user_input)
    total += num
    user_input = input("请输入一个数字，按q进行结束并输出结果:")
if count < 2:
    result = 0
else:
    result = total / count
print(result)