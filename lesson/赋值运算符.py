a = 21
b = 10
c = 0

num1 = c = a + b
print(a, "+", b, "的值为：", c)
c += a
num2 = c
print(num1, "+", a, "的值为：", c)
c *= a
num1 = c
print(num2, "乘以", a, "的值为：", c)
c /= a
num2 = c
print(num1, "除以", a, "的值为：", c)
c = 2
c %= a
num1 = c
print(2, "对", a, "取模的值为：", c)
c **= a
num2 = c
print(num1, "的", a, "次幂的值为：", c)
c //= a
print(num2, "对", a, "取整除的值为：", c)
