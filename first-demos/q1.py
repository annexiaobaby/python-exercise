# 方法 函数
def zjs(x):
    if x%2==1:
        # print('这是一个奇数')
        return True # 返回值
    else:
        # print('这是一个偶数')
        return False

# 程序
def jfc(a, b, c):
    if a == 0:
        print("a不能等于0")
        return

    result_1 = b * b - 4 * a * c
    if result_1 < 0:
        print('delta不能小于0')
        return

    result_2 = result_1 ** 0.5

    x1 = (-b + result_2) / (2 * a)
    x2 = (-b - result_2) / (2 * a)

    print('x1=%s,x2=%s' % (x1, x2))

# 调用程序
if __name__=='__main__':
    jfc(1,-9,20)

    while True:
        x=int(input('请输入一个整数:'))
        if x==6:
            print('程序退出')
            break
        result=zjs(x)
        # if result==True:
        #     print('奇数')
        # else:
        #     print('偶数')
        print('奇数' if result==True else '偶数')