a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
b = {}
for i in range(len(a)):
    print(i+1, a[i])
    b[i+1] = a[i]
print(b)
print(a)
"""
dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tiny1dict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值
print(tiny1dict)  # 输出完整的字典
print(tiny1dict.keys())  # 输出所有键
print(tiny1dict.values())  # 输出所有值

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
print(dict)

del dict['Name']  # 删除键 'Name'
# print("dict['Age']: ", dict['Name'])
print(dict)
dict.clear()  # 清空字典
print(dict)

del dict  # 删除字典
print(dict)
"""
