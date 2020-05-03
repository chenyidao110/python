"""
输出100以内的素数
"""
for num in range(2,100):
    is_prime = True
    for factor in range(2,num):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)