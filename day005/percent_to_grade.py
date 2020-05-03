"""
百分之转换为等级制成绩
"""

score = float(input('请输入成绩：'))

if score >= 98:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif grade >= 70:
    grade = 'C'
elif grade >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是：',grade)