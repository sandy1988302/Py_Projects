sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('aoiuyc')
b = set('sdkcnwa')
print(a)
print(b)
print(a - b)  # a 和 b 的差集
print(b - a)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素
