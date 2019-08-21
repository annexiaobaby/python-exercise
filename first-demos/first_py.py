# 给变量赋值


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


# 用程序
if __name__ == '__main__':
    jfc(1, -7, 12)
