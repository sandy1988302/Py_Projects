import random

# 蛋池抽奖规则：获取SSR的概率为2%；
# 连续50次(black)没有获取SSR，下次SSR概率提升2%，并且每次没有获得SSR都会累加2%，直到获取SSR，回到原始概率2%；
# 获取SSR，一半概率为up_ssr,一半为no_ssr

a = 101  # 抽取1到100的随机数，获得1，2则是获取到ssr，如果脸黑次数大于50，就是a<=(2+d*2)抽取到ssr
up_ssr = 0  # 拿到up_ssr数量
black = 0  # 脸黑次数（1次抽取没有ssr）
no_ssr = 0  # 拿到no_ssr数量
i = 1  # 下一次抽取次数
d = 0  # 连续脸黑50次后开始从0累计，每1次脸黑额外增加获取ssr的概率2%，实际概率为(2+2*d)%
n = (130 + 130 + 66 + 66 + 33 + 33) * 180 / 600  # 200点进行一次蛋池抽奖，计算得出总点数可以抽奖的次数
while i <= n:
    a = random.randint(1, 100)
    if black > 50:
        d = black - 50
    if a <= (2 + d * 2):
        if (a % 2) == 0:
            print('概率' + str(2 + d * 2) + '%,第' + str(i) + '次中奖，拿到你要的up_ssr')
            up_ssr += 1
            black = 0
            d = 0
        else:
            print('概率' + str(2 + d * 2) + '%,第' + str(i) + '次中奖,但是不是你要的：no_ssr')
            no_ssr += 1
            black = 0
            d = 0
    else:
        black += 1
        print('概率' + str(2 + d * 2) + '%,第' + str(i) + '次未中奖')
    i += 1
print('up_ssr获取' + str(up_ssr) + '个，no_ssr获取' + str(no_ssr) + '个')
