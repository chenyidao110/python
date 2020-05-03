"""
判断输入的边长是否构成三角形，如果能则计算出三角形的周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长：{peri}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'面积：{area}')
else:
    print('不能构成三角形')