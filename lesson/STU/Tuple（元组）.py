tuple1 = ('abed', 786, 2.23, 'runoob', 70.2)
tiny1tuple = (123, 'runoob')

print(tuple1)  # 输出完整元组
print(tuple1[0])  # 输出元组的第一个元素
print(tuple1[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple1[2:])  # 输出从第三个元素开始的所有元素
print(tiny1tuple * 2)  # 输出两次元组
print(tuple1 + tiny1tuple)  # 连接元组

tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print("删除后的元组 tup : ")
print(tup)
