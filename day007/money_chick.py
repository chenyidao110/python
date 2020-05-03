"""
百钱百鸡
"""
for x in range(0,21):
    for y in range(0,34):
        z = 100 - x -y
        if x * 5 + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(f'公鸡：{x}只，母鸡：{y}只，小鸡：{z}只')