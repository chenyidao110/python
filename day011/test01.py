import random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0

for _ in range(6000):
    face = random.randint(1,6)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif f5 == 5:
        f5 += 1
    else:
        f6 += 1

print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')