a = 21
b = 10
c = 0

if a == b:
    print(a, "等于", b)
else:
    print(a, "不等于", b)

if a != b:
    print(a, "不等于", b)
else:
    print(a, "等于", b)

if a < b:
    print(a, "小于", b)
else:
    print(a, "大于等于", b)

if a > b:
    print(a, "大于", b)
else:
    print(a, "小于等于", b)

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print(a, "小于等于", b)
else:
    print(a, "大于", b)

if b >= a:
    print(b, "大于等于", a)
else:
    print(b, "小于", a)
