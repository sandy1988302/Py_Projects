counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)
a, b, c = 1, 2, "runoob"

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))

str2 = 'Runoob'

print(str2)  # 输出字符串
print(str2[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str2[0])  # 输出字符串第一个字符
print(str2[2:5])  # 输出从第三个开始到第五个的字符
print(str2[2:])  # 输出从第三个开始的后的所有字符
print(str2 * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str2 + "TEST")  # 连接字符串
