"""
斐波拉契数列
"""
a,b = 1,1

print(a,b,end=' ')

for _ in range(18):
    a,b = b,a+b
    print(b,end=' ')