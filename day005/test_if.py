"""
用户身份验证
"""

username = input('请输入用户名：')
password = input('请输入口令：')

if username == 'test' and password == 'test':
    print('身份验证成功!')
else:
    print('身份验证失败!')