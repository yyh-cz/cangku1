temperature_dict = {"111":36.4,"112":37.4,"113":37.4,"114":38.4,}
for staff_id,temp in temperature_dict.items():
    if temp >= 36:
        print(staff_id)

total = 0
for i in range(1,101):
    #rang括号内的数据，1是起始值，101是结束值，但不会包括101，默认等差为1，在101后面加值可以设置等差值
    total = total + i
print(total)

list = ["今","天","你","吃","了","吗"]
i=0
while i < len(list):
    print(list[i])
    i = i + 1