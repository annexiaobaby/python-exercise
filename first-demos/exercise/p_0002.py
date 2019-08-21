# 【题】编写程序，从键盘获取一个个信息，然后按照下面格式显示
#
# ==================================
# 姓名: dongGe
# QQ:xxxxxxx
# 手机号:131xxxxxx
# 公司地址:北京市xxxx
# ==================================

yourname = input('please input your name:')
yourqq = input('please input your qq:')
yourphone = input('please input your phone:')
yourcompanyaddress = input('please input your company address:')

print('=' * 60)
print('\n姓名:%s\nQQ:%s\n手机号:%s\n公司地址:%s' % (yourname, yourqq, yourphone, yourcompanyaddress))
print("=" * 60)
