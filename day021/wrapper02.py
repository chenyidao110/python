import time
import random

from functools import wraps

#定义装饰器函数，它的参数是被装饰的函数或类
def record_time(func):

    @wraps(func)
    #定义一个带装饰功能(记录被装饰函数的执行时间)的函数
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间：{end - start:.3f}秒')
        return result

    return wrapper

@record_time
def download(filename):
    print(f'开始下载 {filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename} 下载完成.')

@record_time
def upload(filename):
    print(f'开始上传 {filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename} 上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
#取消装饰器
download.__wrapped__('MySQL必知必会.pdf')
upload = upload.__wrapped__
upload('Python从新手到大师.pdf')