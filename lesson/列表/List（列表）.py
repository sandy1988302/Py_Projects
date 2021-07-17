list1 = ['abed', 786, 2.23, 'runoob', 70.2]
tiny1list = [123, 'runoob']

print(list1)  # 输出完整列表
print(list1[0])  # 输出列表第一个元素
print(list1[1:3])  # 从第二个开始输出到第三个元素
print(list1[2:])  # 输出从第三个元素开始的所有元素
print(tiny1list * 2)  # 输出两次列表
print(list1 + tiny1list)  # 连接列表


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[4])
print(nums[0:1])
print(nums[0:4])


list2 = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
# 读取第二位
print("list[1]: ", list2[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print("list[1:-2]: ", list2[1:-2])


list3 = ['Google', 'Runoob', 1997, 2000]
print("第三个元素为 : ", list3[2])
list3[2] = 2001
print("更新后的第三个元素为 : ", list3[2])


list4 = ['Google', 'Runoob', 'Taobao']
list4.append('Baidu')
print("更新后的列表 : ", list4)

list5 = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list5)
del list5[2]
print("删除第三个元素 : ", list5)



