"""
计算指定的年月日是这一年的第几天
"""
def is_leap_year(year):
    """判定指定的年份是不是闰年，平年返回False,闰年返回True"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year,month,date):
    """计算传入的日期是这一年的第几天"""
    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ]
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date


print(which_day(1980,11,28))
print(which_day(1981,12,31))
print(which_day(2010,1,1))
print(which_day(2016,3,1))